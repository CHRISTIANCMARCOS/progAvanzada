# EJERCICIO 16

# Área y Volumen.

# Escriba un programa que comience leyendo un radio, r, del usuario. 
# El programa continúe calculando y mostrando el área de un círculo con radio r y el volumen de una esfera con radio r.
# Use la constante pi en el módulo matemático en su cálculos. 

# Sugerencia: El área de un círculo se calcula utilizando el área de fórmula = πr 2. 
# El volumen de una esfera se calcula utilizando la fórmula volumen = 4/3πr 3.

import math

radio = float(input('Introduzca el valor del radio: '))

area = math.pi * radio**2

vol = (4/3) * math.pi * radio**3

print('El area del circulo es: ', '%.02f' % area)
print('El volumen de la esfera es: ', '%.02f' % vol)


