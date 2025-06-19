from app.db import get_connection

def listar_oficinas():
    """
    Consulta y muestra todas las oficinas registradas en la base de datos.
    """
    # Establecer conexión con la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    # Ejecutar consulta para obtener todas las oficinas
    cursor.execute("SELECT * FROM oficina")
    resultados = cursor.fetchall()

    # Mostrar resultados
    for oficina in resultados:
        print(oficina)

    # Cerrar conexión
    conn.close()


def crear_oficina():
    """
    Solicita al usuario los datos de una nueva oficina y la inserta en la base de datos.
    """
    # Solicitar datos de la oficina al usuario
    entrada = input(
        "Ingrese Ciudad, País, Código Postal, Teléfono, Dirección 1 (separados por coma): "
    )
    datos = list(map(str.strip, entrada.split(",")))  # Elimina espacios innecesarios

    # Solicitar el código de oficina
    codigo = input("Código de oficina: ").strip()

    # Verificar que se ingresaron todos los datos requeridos
    if len(datos) != 5:
        print("Error: Se deben ingresar exactamente 5 datos separados por coma.")
        return

    # Establecer conexión con la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    # Consulta SQL para insertar una nueva oficina
    query = """
    INSERT INTO oficina (codigo_oficina, ciudad, pais, codigo_postal, telefono, linea_direccion1)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    try:
        # Ejecutar inserción
        cursor.execute(query, (codigo, *datos))
        conn.commit()
        print("Oficina creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la oficina: {e}")
    finally:
        # Cerrar conexión
        conn.close()
