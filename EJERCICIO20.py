# Ejercicio 20

# Ley del gas ideal.

# La ley de los gases ideales es una aproximación matemática del comportamiento de los gases como
# cambio de presión, volumen y temperatura. Por lo general, se indica como:

# PV = nRT

# donde P es la presión en Pascales, V es el volumen en litros, n es la cantidad de sustancia en moles,
# R es la constante de gas ideal, igual a 8.314 J mol K, y T es el temperatura en grados Kelvin.

# Escriba un programa que calcule la cantidad de gas en moles cuando el usuario suministra
# La presión, el volumen y la temperatura. Prueba tu programa determinando el número
# de moles de gas en un tanque de buceo. Un tanque de buceo típico contiene 12 litros de gas a
# una presión de 20,000,000 Pascales (aproximadamente 3,000 PSI). La temperatura ambiente es
# aproximadamente 20 grados Celsius o 68 grados Fahrenheit.

# Sugerencia: una temperatura se convierte de Celsius a Kelvin al agregar 273.15
# lo. Para convertir una temperatura de Fahrenheit a Kelvin, deduzca 32 de ella,
# multiplícalo por 5/9 y luego agregue 273.15


presion = int(input('Ingrese la presion en pascales: ',))
volumen = int(input('Ingrese el volumen el m^3: '))
temperatura = float(input('Ingrese la temepratura en Celcius: '))

convdecelakelvin = temperatura + 273.15
consr = 8.314

RT = consr * convdecelakelvin
PV = presion * volumen

n = PV / RT

print('La cantidad de mol es: ', '%.02f' % n)

