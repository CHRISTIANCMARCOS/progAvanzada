# Ejercicio 43

# Caras sobre el dinero.


# Es común para las imágenes de los líderes anteriores de un país u otras personas de la historia significado, aparecer en su dinero.
# Las personas que aparecen en los billetes en los Estados Unidos se enumeran en la tabla.
# Escriba un programa que comience leyendo la denominación de un billete del usuario.
# Luego, su programa debe mostrar el nombre de la persona que aparece en el billete de la cantidad ingresada.
# Se debe mostrar un mensaje de error apropiado si no existe tal nota.

#     Individual                  Cantidad
#     George Washington           $ 1
#     Thomas Jefferson            $ 2
#     Abraham Lincoln             $ 5
#     Alexander Hamilton          $ 10
#     Andrew Jackson              $ 20
#     Ulysses S. Grant            $ 50
#     Benjamin Franklin           $ 100

# Si bien los billetes de dos dólares rara vez se ven en circulación en los Estados Unidos,
# son de curso legal que pueden gastarse como cualquier otra denominación. 
# Los Estados Unidos también ha emitido billetes en denominaciones de $ 500, $ 1,000, $ 5,000 y $ 10,000 para uso público.
# Sin embargo, los billetes de alta denominación no se han impreso desde 1945 y se suspendieron oficialmente en 1969.
# Como resultado, no los consideraremos en este ejercicio.

cantidad = input('Ingrese la cantidad del billete: ')



if cantidad == '1':
    print('George Washington')
elif cantidad == '2':
    print('Thomas Jefferson')
elif cantidad == '5':
    print('Abraham Lincoln')
elif cantidad == '10':
    print('Alexander Hamilton')
elif cantidad == '20':
    print('Andrew Jackson')
elif cantidad == '50':
    print('Ulysses S. Grant')
elif cantidad == '100':
    print('Benjamin Franklin')
else:
    print('Valor de billete no valido o se ha suspendido su uso oficialmente')

    