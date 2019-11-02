# Ejercicio 22

# Área de un triángulo (de nuevo).

# En el ejercicio anterior, creó un programa que calculaba el área de un triángulo
# cuando se conocía la longitud de su base y su altura. También es posible calcular
# El área de un triángulo cuando se conocen las longitudes de los tres lados. Deje s1, s2 y s3
# ser la longitud de los lados. Sea s = (s1 + s2 + s3) / 2. Entonces el área del triángulo
# se puede calcular usando la siguiente fórmula:

# area = s × (s − s1) × (s − s2) × (s − s3)

# Desarrolle un programa que lea las longitudes de los lados de un triángulo del usuario y muestra su área.

import math

s1 = int(input('Ingrese la longitud del lado 1: '))
s2 = int(input('Ingrese la longitud del lado 2: '))
s3 = int(input('Ingrese la longitud del lado 3: '))

s = (s1 + s2 + s3)/2

area = math.sqrt (s * (s - s1) * (s - s2) * (s - s3))

print('El area del triangulo es: ', '%.02f' % area)