# Ejercicio 23

# Área de un polígono regular

# Un polígono es regular si sus lados tienen la misma longitud y los ángulos entre todos
# los lados adyacentes son iguales. El área de un polígono regular se puede calcular usando
# la siguiente fórmula, donde s es la longitud de un lado y n es el número de lados:

# area = n * s**2 // 4 * tan(pi/n)

# Escriba un programa que lea s y n del usuario y luego muestre el área de un
# polígono regular construido a partir de estos valores.

import math

s = float(input('Inserte la longitud del lado: '))
n = float(input('Inserte el numero de lados: '))

arriba = n * (s*2)
abajo = 4 * math.tan(math.pi/n)

area = arriba / abajo

print ('El area del poligono es: ', '%.02f' % area)