# Ejercicio 44

# Fecha de nombre de vacaciones.

mes = input('Ingrese el mes: ')
dia = input('Ingrese el dia: ')

if mes == 'enero' and dia == '1':
    print('Es descanso de año nuevo.')

elif mes == 'septiembre' and dia == '16':
    print('Es descanso de mes de la patria.')

elif mes == 'diciembre' and dia == '25':
    print('Es descanso de navidad.')

else:
    print('El mes y dia introducido no corresponde a un descanso obligatorio.')


