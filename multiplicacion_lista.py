# Multiplicar los elementos de una lista por un numero

def ejecutar():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = []

    multiplicador = float(input("Ingrese el numero multiplicador: "))

    for n in numeros:
        resultado.append(n * multiplicador)

    print("Lista original:", numeros)
    print("Lista multiplicada:", resultado)