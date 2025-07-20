# Importa la clase MongoClient de pymongo para conectarse a la base de datos MongoDB
from pymongo import MongoClient

# Importa el módulo os para acceder a variables de entorno del sistema
import os

# Importa la función load_dotenv para cargar las variables definidas en un archivo .env
from dotenv import load_dotenv

# Carga automáticamente las variables de entorno desde un archivo .env ubicado en el mismo directorio o raíz del proyecto
load_dotenv()

# Obtiene la URI de conexión a MongoDB desde las variables de entorno
# Si no encuentra "MONGO_URI", usará None (y generará error en la siguiente línea si no está definido)
client = MongoClient(os.getenv("MONGO_URI"))

# Accede a la base de datos llamada "teleteach" dentro del servidor MongoDB
db = client["teleteach"]
