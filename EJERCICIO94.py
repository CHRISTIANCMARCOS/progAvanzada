# EJERCICIO 94

# Random Password


# 3Escribe una función que genere una contraseña aleatoria. La contraseña debe tener un
# longitud aleatoria de entre 7 y 10 caracteres. Cada personaje debe ser al azar
# seleccionado de las posiciones 33 a 126 en la tabla ASCII. Tu función no tomará
# cualquier parámetro Devolverá la contraseña generada aleatoriamente como su único resultado.
# Muestra la contraseña generada aleatoriamente en el programa principal de tu archivo. Tu principal
# El programa solo debe ejecutarse cuando su solución no se haya importado a otro archivo.

from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

def randomPassword():
    randomLength = randint(SHORTEST, LONGEST)
    result = ''
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result += randomChar
    return result 

def main(): 
    print("Your random password is: ", randomPassword())

if __name__ == "__name__":
    main()