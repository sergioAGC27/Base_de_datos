from app import crud_oficinas, crud_clientes

def menu():
    while True:
        print("\n=== SISTEMA JARDINEX ===")
        print("1. Listar oficinas")
        print("2. Crear oficina")
        print("3. Listar clientes")
        print("4. Buscar clientes por ciudad")
        print("0. Salir")
        op = input("Seleccione una opción: ")
        if op == "1":
            crud_oficinas.listar_oficinas()
        elif op == "2":
            crud_oficinas.crear_oficina()
        elif op == "3":
            crud_clientes.listar_clientes()
        elif op == "4":
            crud_clientes.buscar_clientes_por_ciudad()
        elif op == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()