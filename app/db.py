import mysql.connector

def get_connection():
    """
    Establece y retorna una conexión a la base de datos MySQL.
    Cambia los valores de host, usuario, contraseña y base de datos según tu entorno.
    """
    return mysql.connector.connect(
        host="localhost",          # Dirección del servidor MySQL
        user="admin",              # Usuario de la base de datos
        password="tu_contraseña",  # Contraseña del usuario
        database="jardineria_db"   # Nombre de la base de datos
    )
