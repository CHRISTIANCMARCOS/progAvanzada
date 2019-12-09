# EJERCICIO 65

# Calcular el perímetro de un polígono.

# Escribe un programa que calcule el perímetro de un polígono. Comience leyendo la x
# e valores y para el primer punto en el perímetro del polígono del usuario. Luego
# continúe leyendo pares de valores x e y hasta que el usuario ingrese una línea en blanco para
# Coordenada x. Cada vez que lea una coordenada adicional, debe calcular el
# distancia al punto anterior y agregarlo al perímetro. Cuando se ingresa una línea en blanco
# para la coordenada x, su programa debe agregar la distancia desde el último punto hacia atrás
# al primer punto al perímetro. Entonces debería mostrar el perímetro total. Muestra
# La entrada y salida se muestra a continuación, con la entrada del usuario en negrita:

# Ingrese la parte x de la coordenada: 0
# Ingrese la parte y de la coordenada: 0
# Ingrese la parte x de la coordenada: (en blanco para salir): 1
# Ingrese la parte y de la coordenada: 0
# Ingrese la parte x de la coordenada: (en blanco para salir): 0
# Ingrese la parte y de la coordenada: 1
# Ingrese la parte x de la coordenada: (en blanco para salir):
# El perímetro de ese polígono es 3.414213562373095

from math import tan, pi
numlados = int(input("Numero de entrada de lados: "))
ladoslongitud = float(input("Ingresar la longitud de un lado: "))
area = numlados * (ladoslongitud ** 2) / (4 * tan(pi / numlados))
print("El area del poligono es: ",area)