from app import app
from utils.db import db

#Crear todas las tablas de la base de datos definidas en los modelos de SQLAlchemy.
with app.app_context():
    db.create_all()
#Ejecuta la aplicación Flask en el servidor local
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
