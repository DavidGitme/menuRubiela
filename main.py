import suma_listas

opcion = ""

while opcion != "0":
    print("")
    print("===== MENU DE ALGORITMOS =====")
    print("1. Sumar elementos de dos listas")
    print("0. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        suma_listas.ejecutar()
    elif opcion == "0":
        print("Hasta luego")
    else:
        print("Opcion no valida")