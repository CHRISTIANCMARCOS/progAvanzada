# Ejercicio 26

# Unidades de tiempo 2.

# En este ejercicio usted revertirá el proceso descrito en el ejercicio previo.
# Desarrolle un programa que comienze por leer una cantidad de segundos introducidos por el usuario.
# Su programa debe desplegar la cantidad equivalente en la forma de DD:HH:MM:SS, donde DD son los dias,
# HH son las horas, MM son los minutos y SS son los segundos. Las horas, minutos y segundos deben estar en formato de 2 digitos 
# con un 0 al inicio, si es necesario.

segundos = int(input('Introduce la cantidad de segundos: '))

SEGUNDOSDIA = 86400
SEGUNDOSHORA = 3600
SEGUNDOSMINUTO= 60

dia = segundos / SEGUNDOSDIA
sdia = segundos % SEGUNDOSDIA
hora = sdia / SEGUNDOSHORA
shora = sdia % SEGUNDOSHORA
minutos = shora / SEGUNDOSMINUTO
sminutos = shora % SEGUNDOSMINUTO

print('La cantidad en formato DD:HH:MM:SS en donde.')
print('DD = dias; HH = horas; MM = minutos; SS = segundos es:')
print('\n','%02d' % dia, ':','%02d' % hora, ':','%02d' % minutos ,':','%02d' % sminutos, ) 