from app.db import get_connection

def listar_oficinas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM oficina")
    resultados = cursor.fetchall()
    for oficina in resultados:
        print(oficina)
    conn.close()

def crear_oficina():
    datos = input("Ingrese Ciudad, País, Código Postal, Teléfono, Dirección 1 (separados por coma): ").split(",")
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO oficina (codigo_oficina, ciudad, pais, codigo_postal, telefono, linea_direccion1)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    codigo = input("Código de oficina: ")
    cursor.execute(query, (codigo.strip(), *map(str.strip, datos)))
    conn.commit()
    print("Oficina creada exitosamente.")
    conn.close()