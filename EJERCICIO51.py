# Ejercicio 51

# Calificación de letras a puntos de calificación.

# En una universidad en particular, las calificaciones con letras se asignan a puntos de calificación en el siguiente conducta:

# Puntos de calificación de letras
#            A +  4.0
#            A    4.0
#            A −  3.7
#            B +  3.3
#            B    3.0
#            B −  2.7
#            C +  2.3
#            C    2.0
#            C −  1.7
#            D +  1.3
#            D    1.0
#            F     0
# Escriba un programa que comience leyendo una calificación de letra del usuario. Entonces tu
# El programa debe calcular y mostrar el número equivalente de puntos de calificación. Asegurar
# que su programa genera un mensaje de error apropiado si el usuario ingresa un mensaje no válido grado de la letra.


letra = input('Ingrese la letra de la calificacion: ')


if letra == 'A+' or letra == 'A':
    print('Sus puntos de calificacion es: 4.0')
elif letra == 'A-':
    print('Sus puntos de calificacion es: 3.7')
elif letra == 'B+':
    print('Sus puntos de calificacion es: 3.3')
elif letra == 'B':
    print('Sus puntos de calificacion es: 3.0')
elif letra == 'B-':
    print('Sus puntos de calificacion es: 2.7')
elif letra == 'C+':
    print('Sus puntos de calificacion es: 2.3')
elif letra == 'C':
    print('Sus puntos de calificacion es: 2.0')
elif letra == 'C-':
    print('Sus puntos de calificacion es: 1.7')
elif letra == 'D+':
    print('Sus puntos de calificacion es: 1.3')
elif letra == 'D':
    print('Sus puntos de calificacion es: 1.0')
elif letra == 'F':
    print('Sus puntos de calificacion es: 0')
else:
    print('Letra de calificacion erronea')
    


