# EJERCICIO 72

# ¿Es una cuerda un palíndromo?.

# Una cadena es un palíndromo si es idéntica hacia adelante y hacia atrás. Por ejemplo "anna",
# “Civic”, “level” y “hannah” son ejemplos de palabras palindrómicas. Escribir un programa
# que lee una cadena del usuario y usa un bucle para determinar si es o no un
# palíndromo. Muestra el resultado, incluido un mensaje de salida significativo.

palabra = input('Introduce una palabra: ')
palindromo = palabra [::-1]
if palindromo == palabra:
    print('La palabra',palabra, 'es palindromo')
else:
    print('La plabra',palabra, 'no es palindromo')