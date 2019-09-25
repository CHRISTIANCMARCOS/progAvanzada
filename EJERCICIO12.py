# EJERCICIO 12.

# Distancia entre dos puntos de la tierra

# La superficie de la tierra es curva y la distancia entre grados de longitud varia con la latitud.
# Como resultado, encontrar la distancia entre dos puntos de la superficie de la Tierra es más 
# complicado que usar el Teorema de Pitágoras.
# Si (t1,g1) y (t2,g2) es la latitud y longitud de dos puntos de la superficie de la Tierra.
# La distancia entre esos puntos, a través de la superficie de la Tierra, en kilometros es:

# distancia= 6371.01*arccos(sen(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2)) 

# Cree un programa que le permita al usuario introducir la latitud y longitud de dos puntos de la Tierra en grados.
# Su programa debe desplegar la distancia entre esos puntos, en kilometros.
# Tenga en cuenta que las funciones trigonometricas de python trabajan en radianes, por lo que debe convertir 
# el valor introducido por el usuario en grados a radianes antes utiliar la formula.
# El modulo math contiene el comando radians, que cambia de grados a radianes.

# 12 11 9 6 640

import math


t1r= float(input('Introduce el valor de la latitud inicial en grados: '))
g1r= float(input('Introduce el valor de la longitud inicial en grados: '))
t2r= float(input('Introduce el valor de la latitud final en grados: '))
g2r= float(input('Introduce el valor de la longitud final en grados: '))

t1rad= math.radians(t1r) 
g1rad= math.radians(g1r) 
t2rad= math.radians(t2r)
g2rad= math.radians(g2r)

st1= math.sin(t1rad)
st2= math.sin(t2rad)
ct1= math.cos(t1rad)
ct2= math.cos(t2rad)

resta= math.cos(g1rad-g2rad)

arco= math.acos(st1*st2+ct1*ct2*resta)

# distancia= 6371.01*arccos(sen(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2)) 

distancia= 6371.01*arco



print('La distancia entre los dos puntos es: ','%.2f ' 'Km' % distancia)
