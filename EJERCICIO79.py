# EJERCICIO 79

# Número entero máximo.

# Este ejercicio examina el proceso de identificación del valor máximo en una colección.
# de enteros. Cada uno de los enteros se seleccionará aleatoriamente de los números entre
# 1 y 100. La colección de enteros puede contener valores duplicados, y algunos de los
# los enteros entre 1 y 100 pueden no estar presentes.
# Tómese un momento y piense cómo manejaría este problema en papel.
# Muchas personas verifican cada número entero en secuencia y se preguntan si el número
# que están considerando actualmente es mayor que el mayor número que han visto
# previamente. Si es así, entonces olvidan el número máximo anterior y recuerdan
# el número actual como el nuevo número máximo. Este es un enfoque razonable,
# y dará como resultado la respuesta correcta cuando el proceso se realice con cuidado. Si tu
# estaban realizando esta tarea, ¿cuántas veces esperaría necesitar actualizar el
# valor máximo y recuerda un nuevo número?
# Si bien podemos responder la pregunta planteada al final del párrafo anterior usando
# teoría de la probabilidad, vamos a explorarla simulando la situación. Crear un
# programa que comienza seleccionando un número entero aleatorio entre 1 y 100. Guarde esto
# entero como el número máximo encontrado hasta ahora. Después de que el entero inicial ha sido
# seleccionado, generar 99 enteros aleatorios adicionales entre 1 y 100. Verifique cada
# entero, ya que se genera para ver si es mayor que el número máximo encontrado
# hasta aquí. Si es así, su programa debería actualizar el número máximo encontrado
# y cuente el hecho de que realizó una actualización. Muestra cada número entero después de ti
# generarlo Incluya una notación con esos enteros que representan un nuevo máximo.
# Después de haber mostrado 100 enteros, su programa debería mostrar el máximo
# valor encontrado, junto con el número de veces que el valor máximo
# fue actualizado durante el proceso. La salida parcial para el programa se muestra a continuación,
# con ... representando los enteros restantes que mostrará su programa. Ejecute su
# programa varias veces. Es el número de actualizaciones realizadas en el valor máximo
# que esperabas

from random import randrange

piezas = 100
mx_value = randrange(1, piezas + 1)
print(mx_value)

num_updates = 0

for i in range(1, piezas):
    current = randrange(1, piezas + 1)
    if current > mx_value:
        mx_value = current
        num_updates = num_updates + 1
        print(current, '<== Update')
    else:
        print(current)
print('El valor máximo encontrado es:', mx_value )
print('El valor máximo fue actualizar: ', num_updates, 'veces')