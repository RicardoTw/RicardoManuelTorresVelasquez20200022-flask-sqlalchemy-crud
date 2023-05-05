from dotenv import load_dotenv
import os

load_dotenv()

# Obtener información de conexión de la base de datos desde variables de entorno.
user = os.environ["USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
database = os.environ["DATABASE"]
server = os.environ["SERVER"]

# Construye la cadena de conexión de la base de datos utilizando las variables de entorno previamente obtenidas
DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)
