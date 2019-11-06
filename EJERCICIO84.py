# Ejercicio 84

# Convertir un numero entero a numero cardinal

# Las palabras como primero, segundo, tercero y cuarto son llamadas como numeros cardinales.
# En este ejercicio debe de escribir una funcion que tome un numero entero como su unico parametro
# y regrese una cadena de caracteres con la palabra cardinal de numero entero insertado. su funcion 
# debe manejar los numeros enteros entre el 1 y el 12 y debe regresar su correspondiente nuero cardinal 
# Incluya un programa principal que demuestre su funcion desplegando cada entero del 1 al 12 y su numero 
# cardinal.

def cardinal(numero):
    if numero == 1:
        car = 'primero'
    elif numero == 2:
        car = 'segundo'
    elif numero == 3:
        car = 'tercero'
    elif numero == 4:
        car = 'cuarto'
    elif numero == 5:
        car = 'quinto'
    elif numero == 6:
        car = 'sesto'
    elif numero == 7:
        car = 'septimo'
    elif numero == 8:
        car = 'octavo'
    elif numero == 9:
        car = 'noveno'
    elif numero == 10:
        car = 'decimo'
    elif numero == 11:
        car = 'onceavo'
    elif numero == 12:
        car = 'doceavo'
    return car
 
num = int(input('Ingrese un numero entero del 1 al 12: '))

cardi = cardinal(num)

print('El cardina es: ',cardi)


