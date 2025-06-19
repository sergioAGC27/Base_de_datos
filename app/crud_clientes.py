from app.db import get_connection

def listar_clientes():
    """
    Muestra la lista de todos los clientes con su código, nombre y ciudad.
    """
    # Establecer conexión con la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    # Ejecutar consulta para obtener todos los clientes
    cursor.execute("SELECT codigo_cliente, nombre_cliente, ciudad FROM cliente")

    # Mostrar resultados
    for row in cursor.fetchall():
        print(row)

    # Cerrar la conexión
    conn.close()


def buscar_clientes_por_ciudad():
    """
    Solicita una ciudad al usuario y muestra los nombres de los clientes que pertenecen a esa ciudad.
    """
    # Solicitar ciudad al usuario
    ciudad = input("Ingrese la ciudad: ").strip()

    # Establecer conexión con la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    # Ejecutar consulta con parámetro para evitar inyección SQL
    cursor.execute(
        "SELECT nombre_cliente FROM cliente WHERE ciudad = %s",
        (ciudad,)
    )

    # Mostrar resultados
    for row in cursor.fetchall():
        print(row)

    # Cerrar la conexión
    conn.close()
