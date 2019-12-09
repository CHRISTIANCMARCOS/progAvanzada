# EJERCICIO 78

# Decimal a Binario.

# Escriba un programa que convierta un numero decimal(base 10)que inserte un usuario como numero y despues use el lograritmo 
# division mostrado para realiar la conversion. Cuando el algoritmo se complete el resultado debera contener la representacion del numero 
# en binario. Despues se debera desplegar el resultado con el mensaje apropiado.

# Sea el resultado una variable string vacia.
# Sea q un numero entero a convertir 

# repetir:
# Sea r igual al residuo cuando q es dividido entre 2.
# Convertir r a string y agregarlo al comienso de resultado.
# Dividir q entre 2, eliminar cualquier residuo y guardar el resultado nuevo en q hasta que q sea cero.

resultado = ''
q = int(input('Inserta el numero:  '))

r = q % 2

resultado = str(r) + resultado
q = q // 2

while q > 0:
    r = q % 2
    resultado = str(r) + resultado
    q = q // 2 

print('binaro', resultado)


