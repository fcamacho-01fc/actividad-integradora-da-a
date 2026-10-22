from datetime import date
import json


ARCHIVO_VENTAS = "datos/ventas.json"


def cargar_ventas():
    try:
        with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error al cargar el archivo de ventas.json")
        return []




def guardar_ventas(registros):
    try:
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as archivo:
            json.dump(registros, archivo)
    except:
        print("Error al guardar el archivo de ventas.json")


def siguiente_id(registros):
   mayor_id =  0
   for registro in registros:
    if registro["id"]!= None and registro["id"] > mayor_id:
        mayor_id = registro["id"]
    if registro["id"]== None:
        return 0
    return mayor_id+1


def registrar_venta():
    registros = cargar_ventas()
    try:
        cantidad = int(input("Cantidad de huevos: "))
        precio = float(input("Precio por producto: "))
    except:
        print("Ingrese datos validos numericos")
        return

    cliente_id = None
    id_cliente = input("Ingrese id del cliente (opcional): ")
    if id_cliente!="":
        try:
            cliente_id = int(id_cliente)
        except ValueError:
            print("Id cliente debe ser numerico, el registro se hara sin cliente")
            cliente_id = None
            return
        except:
            print("Error al verificar id del cliente")
            return
    else:
        import clientes
        clientes_registrados = clientes.cargar_clientes()
        if clientes_registrados != None:
            cliente_existente = False
            for cliente in clientes_registrados:
                if(cliente["id"] == cliente_id):
                    cliente_existente = True
                if not cliente_existente:
                    print("Id cliente no existe, el registro se hara sin cliente")


    ventas = {
        "id": siguiente_id(registros),
        "cantidad": cantidad,
        "precio": precio,
        "fecha": date.today().isoformat(),
        "cliente": cliente_id
    }

    registros.append(ventas)
    guardar_ventas(registros)
    print("Venta guardada")

            

def listar_ventas():
    registros = cargar_ventas()
    if len(registros) == 0:
        print("No hay registros que mostrar")
        return
    for venta in registros:
        total = venta["cantidad"] * venta["precio"]
        print(
            "ID: ", venta["id"],
            "Fecha: ", venta["fecha"],
            "cliente: ", venta["cliente"],
            "Cantidad: ", venta["cantidad"],
            "Precio: ", venta["precio"],
            "Total: ", total,
        )


def buscar_venta():
    registros = cargar_ventas()
    try: 
        venta_id = int(input("Id venta a buscar: "))
    except ValueError:
        print("Ingresa id numerico valido")
        return
    for venta in registros:
        if venta["id"] == venta_id:
            total = venta["cantidad"] * venta["precio"]
            print(
                "ID: ", venta["id"],
                "Fecha: ", venta["fecha"],
                "cliente: ", venta["cliente"],
                "Cantidad: ", venta["cantidad"],
                "Precio: ", venta["precio"],
                "Total: ", total,
                    )
            return
    print("Venta no encontrada")


def actualizar_venta():
    registros = cargar_ventas()
    try:
        venta_id = int(input("Id de venta a actualizar: "))
    except ValueError:
        print("Ingrese id numerico valido")
        return
    for venta in registros:
        if venta_id == venta["id"]:
            try:
                cantidad = int(input("Cantidad de huevos: "))
                precio = float(input("Precio por producto: "))
            except:
                print("Ingrese datos validos numericos")
                return
            venta["cantidad"] = cantidad
            venta["precio"] = precio
            guardar_ventas(registros)
            return

def eliminar_venta():
    pass


def menu_ventas():
    while True:
        print("\nVENTAS")
        print("1. Registrar venta")
        print("2. Listar ventas")
        print("3. Buscar venta")
        print("4. Actualizar venta")
        print("5. Eliminar venta")
        print("6. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            buscar_venta()
        elif opcion == "4":
            actualizar_venta()
        elif opcion == "5":
            eliminar_venta()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_ventas()
