# Escribe un programa que solicite al usuario una cantidad de segundos y muestre
# cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
# hora, 1 minuto y 1 segundo.
secs = int(input("Ingresá una cantidad de segundos: "))
print(f'{secs} equivalen a {secs//3600}h{(secs%3600)//60}m{secs%60}s')