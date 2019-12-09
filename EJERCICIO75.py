# EJERCICIO 75

# Máximo común divisor.

# El máximo común divisor de dos enteros positivos, n y m, es el mayor número,
# d, que se divide uniformemente en n y m. Hay varios algoritmos que pueden ser
# utilizado para resolver este problema, que incluye:
# Inicialice d al menor de m y n.
# Mientras que d no divide equitativamente m o d no divide equitativamente n do
# Disminuya el valor de d en 1
# Informe d como el máximo divisor común de n y m
# Escriba un programa que lea dos enteros positivos del usuario y use este algoritmo
# para determinar e informar su mayor divisor común.

n = int(input('Introduce un numero entero n positivo: '))

m = int(input('Introduce un numero entero m positivo: '))

d = min(n,m)

while n % d !=0 or m % d != 0:
    
    d = d-1

print('El maximo divisor comun de n = ', n, 'y m = ', m,'es:',d )