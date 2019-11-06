# Ejercicio 57

# ¿Es un año bisiesto?.

# La mayoría de los años tienen 365 días. Sin embargo, el tiempo requerido para que la Tierra orbita alrededor del Sol
# en realidad es un poco más que eso. Como resultado, se incluye un día adicional, el 29 de febrero.
# en algunos años para corregir esta diferencia. Dichos años se denominan años bisiestos.
# Las reglas para determinar si un año es o no bisiesto son las siguientes:
# • Cualquier año que es divisible por 400 es un año bisiesto.
# • De los años restantes, cualquier año divisible por 100 no es bisiesto.
# • De los años restantes, cualquier año que sea divisible por 4 es un año bisiesto.
# • Todos los demás años no son bisiestos.
# Escriba un programa que lea un año del usuario y muestre un mensaje que indique
# si es o no un año bisiesto.

año =  int(input("Introduce un año: "))

if año % 400 == 0:
    print('Es un año bisiesto')
elif año % 100 == 0:
    print('No es un año bisiesto')
elif año % 4 == 0:
    print('Es un año bisiesto')
else: 
    print('No es un año bisiesto')

