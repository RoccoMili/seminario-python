# Crea un programa que dado un número N ingresado por el usuario, imprima los
# números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue
# # donde haga falta
N = int(input("Ingresá un número: "))
for num in range(1, N+1):
    if num % 5 == 0:
        continue
    print(num)