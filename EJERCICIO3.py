# Ejercicio 3.

# Área de una habitación

# Escriba un programa que le pregunte al usuario el largo
# y el ancho de una habitacion. una vez que los valores
# han sido leidos, su programa debe calcular y desplegar
# el area de la habitacion. El largo y el ancho debe ser 
# introducido con punto flotante (decimal). Incluya las
# unidades (metros) en su mensaje de entrada y salida.

largo = float(input('\nIngresa el largo en metros de la habitacion:'))
ancho = float(input('\nIngresa el ancho en metros de la habitacion:'))
area = largo*ancho
print('\nEl area de la habitacion es de',area, 'metros cuadrados')