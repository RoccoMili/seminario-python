# Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
# oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
# espacios. Las palabras cortas deben ser excluidas del resultado final
words = (input("Ingresá una lista de palabras, separadas por coma:\n")).split(", ")
result = ''

print('OPCIÓN 1:')
for x in words:
    if len(x) > 3:
        result += f'{x} '
print(result)

print('\nOPCIÓN 2:')
result = " ".join(w.strip() for w in words if len(w.strip()) > 3)
print(result)