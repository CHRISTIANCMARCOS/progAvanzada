# Ejercicio 10.

# Aritmetica 

# Cree un programa que lea dos valores enteros, a y b, introducidos por el usuario.
# Su programa debe calcular y mostrar.

from math import log10

a= int(input('Inserte el valor de a: '))
b= int(input('Inserte el valor de b: '))

suma= a+b
resta= a-b
producto= a*b
cociente= a/b 
residuo= a%b
ln= log10(a)
potencia= a**b

print('\nLa suma de a mas b es: ',suma)
print('La resta de a menos b es: ',resta)
print('El producto de a por b es: ',producto)
print('El cociente de a entre b es es: ',cociente)
print('El residuo de a entre b es: ',residuo)
print('El lograritmo de a es: ', '%.2f' % ln)
print('La potencia a ^ b es: ',potencia)