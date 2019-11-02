# Ejercicio 21

# Área de un triángulo.

# El área de un triángulo se puede calcular usando la siguiente fórmula, donde b es el
# longitud de la base del triángulo, y h es su altura:

# area = b × h / 2

# Escriba un programa que permita al usuario ingresar valores para b y h. El programa
# luego debe calcular y mostrar el área de un triángulo con longitud base b y altura h. 


base = float(input('Ingrese el valor de la base: '))
altura = float(input('Ingrese el valor de la altura: '))

area = base * altura / 2

print('El area del triangulo es: ', '%.02f' % area)

