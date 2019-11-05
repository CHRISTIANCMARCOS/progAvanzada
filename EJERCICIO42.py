# Ejercicio 42

# Frecuencia a tener en cuenta.

# En la pregunta anterior, convertiste del nombre de la nota a la frecuencia. En esta pregunta
# escribirás un programa que invierta ese proceso. Comience leyendo una frecuencia
# del usuario Si la frecuencia está dentro de un Hertz de un valor listado en la tabla en
# En la pregunta anterior, informe el nombre de la nota. De lo contrario, informe que el
# la frecuencia no corresponde a una nota conocida. En este ejercicio solo necesitas
# considere las notas enumeradas en la tabla. No hay necesidad de considerar notas de otros
# octavas

frec = float(input('Ingrese el valor de una frecuencia: '))

if frec >= 261.63 and frec < 293.66:
    print('La nota es C4')
elif frec >= 293.66 and frec < 329.63:
    print('La nota es D4')
elif frec >= 329.63 and frec < 349.23:
    print('La nota es E4')
elif frec >= 349.23 and frec < 392.00:
    print('La nota es F4')
elif frec >= 392.00 and frec < 440.88:
    print('La nota es G4')
elif frec >= 440.00 and frec < 493.88:
    print('La nota es A4')
elif frec == 493.88:
    print('La nota es B4')
else: 
    print('La frecuencia no corresponde a una nota conocida')



