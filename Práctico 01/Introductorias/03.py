# Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
# del 1 al 10 utilizando un bucle for
num = int(input("Ingresá un número: "))
for curr in range(1, 11):
    print(f'{num} * {curr} = {num*curr}')