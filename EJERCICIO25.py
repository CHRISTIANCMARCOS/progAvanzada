# Ejercicio 25

# Unidades de tiempo 

# Crear un programa que le pida al usuario la duración de días, horas, minutos y segundos.
# Calcular y desplegar la cantidad total de segundos de duaración.

dias= int(input('Inserte la cantidad de dias: '))
horas= int(input('Inserte la cantidad de horas: '))
minutos= int(input('Inserte la cantidad de minutos: '))
segundos= int(input('Inserte la cantidad de segundos: '))

d=dias * 86400
h=horas * 3600
m=minutos * 60
s=segundos

total=d + h + m + s

print('El total de segundos total es: ', total)