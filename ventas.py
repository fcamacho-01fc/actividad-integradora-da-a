from datetime import date
import json


ARCHIVO_VENTAS = "datos/ventas.json"


def cargar_ventas():
    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
   


def guardar_ventas(registros):
    with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as archivo:
        json.dump(registros, archivo)
    


def siguiente_id(registros):
   pass


def registrar_venta():
    pass
            

def listar_ventas():
    pass


def buscar_venta():
    pass


def actualizar_venta():
    pass



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
