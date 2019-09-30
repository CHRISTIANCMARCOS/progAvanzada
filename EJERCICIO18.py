# EJERCICIO 18

# Volumen de un cilindro.

# El volumen de un cilindro se puede calcular multiplicando el área de su circular
# base por su altura. Escriba un programa que lea el radio del cilindro, junto con
# su altura, desde el usuario y calcula su volumen. Mostrar el resultado redondeado a uno
# decimal.


r=float(input('Introduzca el valor del radio en metros: '))
h=float(input('Introduzca el valor de la altura en metros: '))


pi= 3.1416
radiocuadrado= r**2
area= pi * radiocuadrado
volumen= area * h

print('El volumen del cilindro es: ','%.1f' ' metros' % volumen)