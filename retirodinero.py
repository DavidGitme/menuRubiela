saldo = float(input("Ingrese el saldo de la cuenta: "))
retiro = float(input("Ingrese el valor a retirar: "))

if retiro > saldo:
    print("Saldo insuficiente para realizar el retiro.")
elif retiro <= 0:
    print("El valor del retiro debe ser mayor a cero.")
else:
    saldo_restante = saldo - retiro
    print(f"Retiro exitoso. Saldo restante: {saldo_restante}")