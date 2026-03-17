# Escribe un programa que simule una caja registradora: el usuario ingresa precios de
# productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
# acumulado. Nota: utilizá la sentencia break cuando haga falta.

print('A partir de ahora, ingresá precios de productos. Introducí 0 para cerrar.')
accumulator = 0

while True:
    current = float(input("PRECIO: "))
    if current == 0:
        break
    accumulator += current

print(f"ACUMULADO: {accumulator if accumulator != 0 else 'No se introdujo nada'}")