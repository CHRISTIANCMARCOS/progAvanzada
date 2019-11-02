# Ejercicio 34


# Escriba un programa que lea un numero entero introducido por el usuario.
# Su programa debe desplegar un mensaje indicando si su numero entero es par o impar.

entero = int(input('Ingrese un número entero: '))

b = entero % 2

if b == 0 :
    print('Es par')
else:
    print('Es impar')

