# Ejercicio 46

# El ejercicio esta dividido  en cuatro temporadas:
# primavera, verano, otoño e invierno.
# Aunque las fechas exactas cambian un poco 
# dependiendo del año, usemos las siguientes
# fechas:

# Temporada       Primer dia 
# __________________________
# Primavera       Marzo 21
# Verano          Junio 21
# Otoño           Septiembre 22
# Invierno        Diciembre 21

# Escriba un programa en el que el usuario introduzca el mes y el dia. El usuario introducira el nombre del mes como una *string* 
# seguido del dia como un entero *int*. Su programa debe desplegar la temporada de acuerdo ala informacion introducida por el usuario.


mes = input('Introduzca el mes: ')
dia = int(input('Introduzca el dia: '))



temporada = '' 


if mes == 'marzo' and dia >= 21:
    temporada = 'Primavera'
elif mes == 'abril' or mes == 'mayo':
    temporada = 'Primavera'
elif mes == 'junio' and dia < 21:
    temporada = 'Primavera'
if mes == 'junio' and dia >= 21:
    temporada = 'Verano'
elif mes == 'julio' or mes == 'agosto':
    temporada = 'Verano'
elif mes == 'septiembre' and dia < 22:
    temporada = 'Verano'
if mes == 'septiembre' and dia >= 22:
    temporada = 'Otoño'
elif mes == 'octubre' or mes == 'noviembre':
    temporada = 'Otoño'
elif mes == 'diciembre' and dia < 21:
    temporada = 'Otoño'
if mes == 'diciembre' and dia >= 21:
    temporada = 'Invierno'
elif mes == 'enero' or mes == 'febrero':
    temporada = 'Invierno'
elif mes == 'marzo' and dia < 21:
    temporada = 'Invierno'

print('',temporada)