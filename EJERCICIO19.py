# EJERCICIO 19

#

# Escriba un programa que determine como un objeto viaja cuando golpea el piso. El usuario insertara la informacion de la altura 
# desde donde el objeto se deja caer, en metros(m). Dado que el objeto se deja caer desde el reposo (velocidad inicial V0=0 m/s).
# Asumiendo que la aceleracion debido a la gravedad es 9.81 m/s^2 y usando la formula vf=sqrt(vo^2+2gd) calcule la velocidad final 
# vf usando la velocidad inicial vo la aceleracion g , y la distancia d.


import math

d= float(input('\nInsertar la altura de donde se deja caer el objeto: '))

Vo= 0

g= 9.81

vf= math.sqrt(Vo*Vo)+math.sqrt(2*g*d)


print('La velocidad final es: ','%.2F ' 'm/s' % vf)