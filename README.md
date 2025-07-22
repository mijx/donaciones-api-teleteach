# 💸 TeleTeach – API de Donaciones

Este repositorio contiene el microservicio `donaciones-api-teleteach`, encargado de gestionar las donaciones de los usuarios en la plataforma **TeleTeach**.

Forma parte del ecosistema **TeleTeach**, desarrollado como parte del curso _Ingeniería de Software 2 – 2025-1_, bajo una arquitectura tipo SOFEA (Start-end Only Front-End Architecture).

---

## 🚀 Tecnologías utilizadas

- Python 3.11+
- Flask
- MongoDB (vía `pymongo`)
- Swagger UI (con Flasgger)
- Prometheus (para métricas)
- Dotenv (opcional, para configuración)

---

## ⚙️ Instalación y ejecución local

```bash
# Clona el repositorio
git clone https://github.com/mijx/donaciones-api-teleteach
cd donaciones-api-teleteach

# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
python app.py
```
La documentación en Swagger se encuentra en: http://localhost:8888/docs/
## 📋 Endpoints principales
| Método | Ruta              | Descripción                           |
|--------|-------------------|----------------------------------------|
| POST   | `/donate`         | Registrar una nueva donación           |
| GET    | `/donations`      | Obtener donaciones por correo          |
| DELETE | `/delete_donation`| Eliminar una donación por ID           |
| GET    | `/metrics`        | Exponer métricas para Prometheus       |
| GET    | `/docs/`          | Documentación Swagger generada         |

## 📊 Métricas Prometheus
El endpoint /metrics expone las siguientes métricas:

* Total de peticiones HTTP (http_requests_total)

* Latencia por endpoint (http_request_duration_seconds)

* Errores por endpoint (http_request_errors_total)

Estas métricas pueden ser visualizadas fácilmente en Grafana.

## 🔗 Repositorios relacionados
* 🔐 [API de Autenticación](https://github.com/javiierbarco/auth-api-teleteach)
* 👥 [Repositorio de testing](https://github.com/mijx/testing-teleteach/tree/main)
* 🎓 [API de Cursos y Progreso](https://github.com/javiierbarco/courses-api-teleteach)
* 🧠 [Frontend TeleTeach](https://github.com/javiierbarco/frontend-teleteach)

## 👥 Equipo Castores – Ingeniería de Software 2
Diego H. Lavado G.

Estephanie Perez M.

Frank S. Pardo A.

Javier E. González V.

Juan D. Rivera B.

Victor M. Torres A.

Wullfredo J. Barco G.