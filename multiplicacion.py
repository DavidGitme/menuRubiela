def ejecutar():
    # Solicitamos un número al usuario
    numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))

    print(f"\n--- Tabla de multiplicar del {numero} ---")

    # Usamos un ciclo for que va del 1 al 10
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")