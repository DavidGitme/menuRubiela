# 27. Sumar elementos de dos listas

def ejecutar():
    lista1 = [5, 10, 15, 20, 25]
    lista2 = [35, 40, 45, 50, 55]
    resultado = []

    i = 0
    while i < len(lista1):
        suma = lista1[i] + lista2[i]
        resultado.append(suma)
        i = i + 1

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Resultado:", resultado)