# Ejercicio 61

# Promedio.

# En este ejercicio usted creara un programa que calcule el promedio de una coleccion de valores 
# insertados por el usuario, si el usuario introduce el valor 0 el programa debe dejar de pedir valores y 
# posteriormente mostrar el promedio calculado.

a = 1
sumatoria = 0
i = 0

while a != 0:
    a = int(input('Inserte un valor: '))
    sumatoria = sumatoria + a
    i = i + 1 

promedio = sumatoria / (i - 1)

print('El promedio es: ', promedio)
