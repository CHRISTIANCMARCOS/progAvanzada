# Ejercicio 29

# Celsius a Fahrenheit y Kelvin

# Escriba un programa que comience leyendo la temperatura del usuario en grados
# Celsius. Entonces su programa debe mostrar la temperatura equivalente en grados
# Fahrenheit y grados Kelvin. Los cálculos necesarios para convertir entre diferentes
# unidades de temperatura se pueden encontrar en internet.

Celsius = float(input('Ingrese los grados celcius a convertir: '))

K = Celsius + 273.15

F = (9/5) * Celsius + 32

print('El valor en grados Fahrenheit es: ', F)
print('El valor en grados Kelvin es: ', K)