# EJERCICIO 5.

# Depositos de botellas

# En muchas jurisdicciones se agrega un pequeño depósito a los envases de bebidas para alentar a las personas
# para reciclarlos. En una jurisdicción particular, los recipientes de un litro o
# menos tienen un depósito de $ 0.10, y los recipientes de bebidas que contienen más de un litro tienen
# un depósito de $ 0.25.
# Escriba un programa que lea el número de botellas de cada tamaño que ingresa el usuario.
# Su programa debe continuar calculando y mostrando el reembolso que será
# recibido por devolver esos contenedores. Formatee la salida para que incluya un dólar
# y siempre muestra exactamente dos decimales.


menosde1= 0.10
masde1= 0.25
menos= float(input('\nIngresar botellas de menos de 1 litro: '))
mas= float(input('Ingresar botellas de mas de un litro: '))

menosccm= menos * menosde1
masccm= mas * masde1

sumadebotellas= menosccm + masccm

print('El total es: ', '%.2f'' dolares' % sumadebotellas)

