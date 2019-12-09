# EJERCICIO 77

# Binario a decimal.

# Escriba un programa que convierta un número binario (base 2) a decimal (base 10). Tu
# El programa debe comenzar leyendo el número binario del usuario como una cadena. Luego
# debe calcular el número decimal equivalente procesando cada dígito en el
# número binario. Finalmente, su programa debe mostrar el número decimal equivalente
# con un mensaje apropiado

def binarioadecimal(binario):
    decimal = 0
    for i in range(len(binario)): 
        decimal = decimal + int(binario[i])* 2**(len(binario)- i - 1)
    return decimal

binario = input("Ingrese el número binario que desea convertir: ")

i = 0
while i < len(binario): 
    if (binario[i] != "0") and (binario[i] != "1"):
        print("El valor ingresado no es un número binario")
        binario = input("Ingrese el número binario que desea convertir: ")
        i = 0
    else: 
        i = i+1

print(binarioadecimal(binario))