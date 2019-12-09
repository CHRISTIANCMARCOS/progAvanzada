# EJERCICIO 97

# Buena contraseña aleatoria

# Usando sus soluciones para los Ejercicios 94 y 96, escriba un programa que genere un azar
# buena contraseña y la muestra. Cuente y muestre el número de intentos que fueron
# necesario antes de que se generara una buena contraseña. Estructura tu solución para que
# importa las funciones que escribió anteriormente y luego las llama desde una función
# llamado main en el archivo que crea para este ejercicio.

from ejercicio94 import randomPassword
from ejercicio96 import checkPassword

def main(): 
    n = 0
    passw = ''
    while not checkPassword(passw): 
        passw = randomPassword()
        n = n+1
    print("Intentos: ", n)
    print("Password: ", passw)
    
main()