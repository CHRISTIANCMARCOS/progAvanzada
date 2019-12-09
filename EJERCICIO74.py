# EJERCICIO 74

# Tabla de multiplicación.

# En este ejercicio creará un programa que muestra una tabla de multiplicación que
# muestra los productos de todas las combinaciones de enteros desde 1 por 1 hasta
# 10 veces 10. Su tabla de multiplicar debe incluir una fila de etiquetas en la parte superior
# contiene los números del 1 al 10. También debe incluir etiquetas a la izquierda
# lado que consiste en los números del 1 al 10. La salida esperada del programa
# se muestra a continuación:

# Tabla en libro.

# Al completar este ejercicio, probablemente le resulte útil poder
# imprime un valor sin pasar a la siguiente línea. Esto se puede lograr
# agregando end = "" como el último parámetro a su declaración de impresión. Por ejemplo,
# imprimir ("A") reducirá la letra A y luego bajará a la siguiente línea. los
# la instrucción de impresión ("A", end = "") cambia la letra A sin moverse hacia abajo
# a la siguiente línea, haciendo que la siguiente declaración de impresión muestre su resultado en la misma línea
# como la letra A.

min = 1
max = 10
print('     ',end='')
for i in range(min, max +1):
    print('%4d' % i, end=' ')
print()

for i in range(min, max +1):
    print('%4d' % i, end=' ')
    for j in range(min, max +1):
        print('%4d' %(i*j), end=' ')
    print()