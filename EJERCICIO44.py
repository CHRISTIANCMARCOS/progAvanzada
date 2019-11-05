# Ejercicio 44

# Fecha de nombre de vacaciones.

# Canadá tiene tres feriados nacionales que caen en las mismas fechas cada año.
# Fecha de vacaciones

# Día de año nuevo 1 de enero
# Canadá día 1 de julio
# Día de navidad 25 de diciembre

# Escriba un programa que lea un mes y un día del usuario. Si el mes y el dia
# coincidir con uno de los días festivos enumerados anteriormente, entonces su programa debería mostrar
# nombre de vacaciones De lo contrario, su programa debe indicar que el mes ingresado y
# día no corresponde a un día festivo de fecha fija.
# Canadá tiene dos feriados nacionales adicionales, el Viernes Santo y el Día del Trabajo,
# cuyas fechas varían de año en año. También hay numerosos provinciales y
# vacaciones territoriales, algunas de las cuales tienen fechas fijas, y algunas de las cuales tienen
# Fechas variables. No consideraremos ninguno de estos días festivos adicionales en este
# ejercicio.

mes = input('Ingrese un mes: ')
dia = int(input('Ingrese un dia: '))

if mes == 'enero' and dia == 1:
    print('Dia de año nuevo')
elif mes == 'julio' and dia == 1:
    print('Dia canada')
elif mes == 'diciembre' and dia == 25:
    print('Dia de navidad')
else:
    print('El mes ingresado y dia no corresponde a un dia festivo de fecha fija')
