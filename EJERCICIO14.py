# EJERCICIO 14

# Unidades de altura.

# Muchas personas piensan en su altura en pies y pulgadas, incluso en algunos países que
# utiliza principalmente el sistema métrico. Escriba un programa que lea un número de pies de
# el usuario, seguido de varias pulgadas. Una vez que se leen estos valores, su programa
# debe calcular y mostrar el número equivalente de centímetros.

# Sugerencia: un pie mide 12 pulgadas. Una pulgada es 2.54 centímetros.

f = float(input('Introduzca el valor en pies de su altura: '))

p = float(input('Introduzca el valor en pulgadas de su altura: '))

pie = f * 12 * 2.54
pulgada = p * 2.54

suma = pie + pulgada 

print('La estatura en cm es: ','%.02f' ' centimetros' % suma)

