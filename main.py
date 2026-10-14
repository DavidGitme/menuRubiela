import suma_listas
import multiplicacion
import multiplicacion_lista
 
opcion = ""
 
while opcion != "0":
    print("")
    print("===== MENU DE ALGORITMOS =====")
    print("1. Sumar elementos de dos listas")
    print("2. Tabla de multiplicar")
    print("3. Multiplicar elementos de una lista")
    print("0. Salir")
 
    opcion = input("Elige una opcion: ")
 
    if opcion == "1":
        suma_listas.ejecutar()
    elif opcion == "2":
        multiplicacion.ejecutar()
    elif opcion == "3":
        multiplicacion_lista.ejecutar()
    elif opcion == "0":
        print("Hasta luego")
    else:
        print("Opcion no valida")