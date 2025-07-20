import sys
import os
#  Importa Flask y CORS para crear y exponer la API
from flask import Flask
from flask_cors import CORS

import time
from flask import request, Response
from prometheus_client import Counter, Histogram, generate_latest


#  Asegura que Python trate este directorio como raíz para imports como core.db
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Obtiene la ruta absoluta del directorio actual
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)  # Inserta esa ruta al inicio del sys.path para que los imports funcionen correctamente


#  Importa las rutas definidas para donaciones
from routes.donate import donations

#  Crea la aplicación Flask
app = Flask(__name__)

# === MÉTRICAS PROMETHEUS ===
REQUEST_COUNTER = Counter('http_requests_total', 'Total de peticiones HTTP', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Duración de peticiones HTTP', ['method', 'endpoint'])
ERROR_COUNTER = Counter('http_request_errors_total', 'Errores HTTP por endpoint', ['method', 'endpoint', 'status'])

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    latency = time.time() - request.start_time
    method = request.method
    endpoint = request.path
    status = response.status_code

    REQUEST_COUNTER.labels(method=method, endpoint=endpoint).inc()
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)
    if status >= 400:
        ERROR_COUNTER.labels(method=method, endpoint=endpoint, status=str(status)).inc()

    return response

# Endpoint para Prometheus
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")



#  Habilita CORS para permitir solicitudes desde el frontend
CORS(app)

#  Registra el blueprint que maneja las rutas de donaciones
app.register_blueprint(donations)

# Ejecuta la aplicación si se corre directamente con `python app.py`
if __name__ == "__main__":
    app.run(debug=True, port=8888)  # El modo debug permite ver errores en tiempo real (no usar en producción)
