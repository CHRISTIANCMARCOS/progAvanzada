# EJERCICIO 86

# Los doce días de navidad.

# Los doce días de Navidad es una canción repetitiva que describe una creciente
# larga lista de regalos enviados al verdadero amor en cada uno de los 12 días. Se envía un solo regalo el
# el primer día. Se agrega un nuevo regalo a la colección cada día adicional, y luego
# Se envía la colección completa. Los primeros tres versos de la canción se siguen a continuación.
# Las letras completas están disponibles en internet.
# En el primer día de navidad
# mi verdadero amor me envió:
# Una perdiz en un peral.
# En el segundo día de navidad
# mi verdadero amor me envió:
# Dos tórtolas,
# Y una perdiz en un peral.
# En el tercer día de navidad
# mi verdadero amor me envió:
# Tres gallinas francesas
# Dos tórtolas,
# Y una perdiz en un peral.
# Su tarea es escribir un programa que muestre la letra completa de Los doce
# Días de navidad. Escribe una función que tomo el número del verso como su único parámetro
# y muestra el verso especificado de la canción. Luego llame a esa función 12 veces con
# enteros que aumentan de 1 a 12.
# Cada elemento que se envía al destinatario en la canción solo debe aparecer una vez en su
# programa, con la posible excepción de la perdiz. Puede aparecer dos veces si eso
# te ayuda a manejar la diferencia entre "Una perdiz en un peral" en el primer verso
# y "Y una perdiz en un peral" en los versos posteriores.

from int_ordinal import intToOrdinal

def displayVerse (n):
    print('un', intToOrdinal(n), 'dia de navidad')
    print('Mi verdadero amor me envio: ')

    if n >= 12:
        print('doce bateristas tamborileando,')
    if n >= 11:
        print('once gaiteros giteando,')
    if n >= 10:
        print('diez señores saltando,')
    if n >= 9:
        print('nueve señoras bailando')
    if n >= 8:
        print('ocho criadas un ordeño')
    if n >= 7:
        print('siete nadadores nadando')
    if n >= 6:
        print('seis gansos colocados')
    if n >= 5:
        print('5 anillos de oro')
    if n >= 4:
        print('cuatro aves voladoras')
    if n >= 3:
        print('tres gallinas francesas')
    if n >= 2:
        print('dos tortolas')
    if n >= 1:
        print('A', end=' ')
    else:
        print('y una ', end=' ')
    print('perdiz en un peral')
    print()
def main():
    for verse in range (1, 13):
        displayVerse(verse)
main()