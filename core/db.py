# Importa la clase MongoClient del paquete pymongo, que permite conectarse a un servidor de MongoDB
from pymongo import MongoClient

# Importa el módulo os para acceder a las variables de entorno del sistema operativo
import os

# Importa la función load_dotenv, que carga automáticamente las variables definidas en un archivo .env
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env ubicado en la raíz del proyecto
load_dotenv()

# Obtiene la URI de conexión a MongoDB desde la variable de entorno MONGO_URI
# Si no se encuentra definida en el entorno, usará por defecto "mongodb://localhost:27017/"
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Crea una instancia de conexión al servidor MongoDB utilizando la URI especificada
client = MongoClient(MONGO_URI)

# Selecciona la base de datos llamada "teleteach" en el servidor
# Si no existe, MongoDB la crea automáticamente cuando se inserta un documento
db = client["teleteach"]
