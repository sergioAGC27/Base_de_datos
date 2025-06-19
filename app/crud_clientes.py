from app.db import get_connection

def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo_cliente, nombre_cliente, ciudad FROM cliente")
    for row in cursor.fetchall():
        print(row)
    conn.close()
    
def buscar_clientes_por_ciudad():
    ciudad = input("Ingrese la ciudad: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_cliente FROM cliente WHERE ciudad = %s", (ciudad.strip(),))
    for row in cursor.fetchall():
        print(row)
    conn.close()