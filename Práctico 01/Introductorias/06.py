# Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
# una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
# finalizar
N = int(input("Ingresá un número: "))
multiplos_cinco = []
resto_numeros = []
for num in range(1, N+1):
    if num % 5 == 0:
        multiplos_cinco.append(num)
    else:
        resto_numeros.append(num)
print(multiplos_cinco)
print(resto_numeros)