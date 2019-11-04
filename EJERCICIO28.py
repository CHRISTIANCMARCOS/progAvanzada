# Ejercicio 28

# Escalofríos.

# Cuando el viento sopla en clima frío, el aire se siente aún más frío de lo que realmente es porque el movimiento del aire aumenta la velocidad de enfriamiento 
# de los objetos calientes, como personas. Este efecto se conoce como sensación térmica. En 2001, Canadá, el Reino Unido y los Estados Unidos adoptaron lo siguiente
# fórmula para calcular el índice de sensación térmica. Dentro de la fórmula Ta está el La temperatura del aire en grados Celsius y V es la velocidad del viento en 
# kilómetros por hora. Se puede usar una fórmula similar con diferentes valores constantes con temperaturas en grados Fahrenheit y velocidades del viento en millas por hora.

# WCI = 13.12 + 0.6215Ta - 11.37V0.16 + 0.3965TaV0.16

# Escriba un programa que comience leyendo la temperatura del aire y la velocidad del viento del usuario. Una vez que se hayan leído estos valores, 
# su programa debería mostrar la sensación térmica índice redondeado al entero más cercano. El índice de enfriamiento del viento solo se considera 
# válido para temperaturas inferiores o igual a 10 grados centígrados y velocidades del viento superiores a 4,8 kilómetros por hora.

ta = float(input('Ingrese temperatura aire: '))
vv = float(input('ingrese velocidad viento: '))

WCI = 13.12 + (0.6215 * ta) - (11.37 * (vv ** 0.16)) + (0.3905 * ta * (vv ** 0.16))

print('La sensacion termica es: ', '%.0f' % WCI)

