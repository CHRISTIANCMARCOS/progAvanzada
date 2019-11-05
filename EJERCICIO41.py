# Ejercicio 41 

# Nota a frecuencia.

#     Nota             Frecuencia (Hz)
#     C4                   261.63
#     D4                   293.66
#     E4                   329.63
#     F4                   349.23
#     G4                   392.00
#     A4                   440.00
#     B4                   493.88

# Comience escribiendo un programa que lea el nombre de una nota del usuario y muestra la frecuencia de la nota. 
# Su programa debe admitir todas las notas enumeradas previamente.
# Una vez que tenga su programa funcionando correctamente para las notas enumeradas anteriormente,
# debería agregar soporte para todas las notas de C0 a C8. Si bien esto podría hacerse por
# agregando muchos casos adicionales a su declaración if, tal solución es engorrosa,
# inelegante e inaceptable para los propósitos de este ejercicio. En cambio, deberías
# explotar la relación entre notas en octavas adyacentes. En particular, la frecuencia
# de cualquier nota en octava n es la mitad de la frecuencia de la nota correspondiente en octava n + 1.
# Al usar esta relación, debería poder agregar soporte para las notas adicionales
# sin agregar casos adicionales a su declaración if.
# Sugerencia: para completar este ejercicio, deberá extraer caracteres individuales
# del nombre de la nota de dos caracteres para que pueda trabajar con la letra y
# El número de octava por separado. Una vez que haya separado las partes, calcule
# frecuencia de la nota en la cuarta octava utilizando los datos de la tabla anterior.
# Luego divida la frecuencia por 24 − x, donde x es el número de octava ingresado por
# el usuario. Esto reducirá a la mitad o duplicará la frecuencia la cantidad correcta de veces.

print('Las notas admitidas son:')
print('C4, D4, E4, F4, G4, A4, B4')
nota = input('Ingrese el nombre de una nota para ver su frecuencia: ')

if nota == 'C4':
    print('La frecuencia es 261.63 Hz')
elif nota == 'D4':
    print('La frecuencia es 293.66 Hz')
elif nota == 'E4':
    print('La frecuencia es 329.63 Hz')
elif nota == 'F4':
    print('La frecuencia es 349.23 Hz')
elif nota == 'G4':
    print('La frecuencia es 392.00 Hz')
elif nota == 'A4':
    print('La frecuencia es 440.00 Hz')
elif nota == 'B4':
    print('La frecuencia es 493.88 Hz')

