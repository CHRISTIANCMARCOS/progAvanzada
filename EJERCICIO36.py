# Ejercicio 36

# Vocal o Consonante.

# En este ejercicio creará un programa que lee una letra del alfabeto del usuario. 
# Si el usuario ingresa a, e, i, o, u, entonces su programa debería mostrar un mensaje indicando que la letra ingresada es una vocal. 
# Si el usuario ingresa y entonces su programa debería mostrar un mensaje que indique que a veces y es una vocal, y a veces y es una consonante. 
# De lo contrario, su programa debería mostrar un mensaje que indica que la letra es una consonante.

letra = input('Ingrese una letra del alfabeto: ')

vocal = 'a,e,i,o,u'
ye = 'y'

if letra in vocal:
    print ('Es una vocal')

elif letra in ye:
    print('Aveces y es una vocal o consonate')

else:
    print('Es una consonante')

