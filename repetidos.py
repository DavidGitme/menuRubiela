
def ejecutar():
    nums = [1, 2, 3, 1, 4, 6, 6, 5, 1, 3, 10, 10, 11, 45, 11, 45]

    no_repetidos = []

    for numero in nums:
        if numero not in no_repetidos:
            no_repetidos.append(numero)

    print(f"Lista original: {nums}")
    print(f"Lista sin repetidos: {no_repetidos}")


ejecutar()
