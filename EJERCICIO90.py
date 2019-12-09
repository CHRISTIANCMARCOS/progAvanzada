# EJERCICIO 90

# ¿Una cadena representa un número entero?

# En este ejercicio escribirá una función llamada isInteger que determina
# si los caracteres en una cadena representan o no un número entero válido. Al determinar
# Si una cadena representa un número entero, debe ignorar cualquier espacio en blanco inicial o final.
# Una vez que se ignora este espacio en blanco, una cadena representa un número entero si su longitud es al menos
# 1 y solo contiene dígitos, o si su primer carácter es + o - y el primero
# el carácter es seguido por uno o más caracteres, todos los cuales son dígitos.
# Escriba un programa principal que lea una cadena del usuario e informe si o
# No representa un número entero. Asegúrese de que el programa principal no se ejecutará si el archivo
# que contiene su solución se importa a otro programa.

def es_entero (s):
    s = s.strip()

    if (s[0] == '+' or s[0] == '-' and s[1:].isdigit()):
        return True
    
    if s.isdigit():
        return True
    return False

def main():
    s = input ('Introduce la cadena: ')
    if es_entero(s):
        print('La cadena representa un entero.')
    else:
        print('La cadena no es un entero.')
if __name__ == '__main__':
    main()