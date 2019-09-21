# Ejercicio 4.

# Área de un campo

# Crear un programa que lea el largo y el ancho de un campo de cultivo,
# introducido por el usuario y despliegue el area del campo en acres.

# 1 acre = 4046.86 metros cuadrados

largo = float(input('\nIntroduce el largo del campo en metros:'))
ancho = float(input('\nIntroduce el ancho del campo en metros:'))

area = largo*ancho
acre = 4046.86
conversion = area/acre


print('\nEl area del campo es de',conversion, 'acres')