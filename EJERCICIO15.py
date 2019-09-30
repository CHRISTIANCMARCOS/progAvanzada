# EJERCICIO 15

# Unidades de distancia.

# En este ejercicio, creará un programa que comienza leyendo una medida en pies del usuario. 
# Entonces su programa debe mostrar la distancia equivalente en pulgadas, yardas y millas. 
# Use Internet para buscar los factores de conversión necesarios si no los tienes memorizados.

pies= int(input('Introduzca una medida en pies: '))

p = 12
pulg= pies * p
y = 3
yardas= pies / y
m = 1760 
millas= yardas / m

print ('El valor en pulgadas es: ', pulg)
print ('El valor en yardas es: ', '%.02f' % yardas)
print ('El valor en millas es: ', '%.02f' % millas)