# Ejercicio 47

# Fecha de nacimiento astrologica. 

# Los horóscopos comúnmente reportados en los periódicos usan la posición del sol en el momento del nacimiento para intentar predecir el futuro.
# Este sistema de astrología divide el año en doce signos del zodiaco, como se describe en la tabla a continuación:

# Signo del zodiaco           Rango de fechas
# Capricornio                 22 de diciembre al 19 de enero
# Acuario                     del 20 de enero al 18 de febrero
# Piscis                      del 19 de febrero al 20 de marzo
# Aries                       21 de marzo al 19 de abril
# Tauro                       del 20 de abril al 20 de mayo
# Géminis                     del 21 de mayo al 20 de junio
# Cáncer                      21 de junio al 22 de julio
# Leo                         del 23 de julio al 22 de agosto
# Virgo                       del 23 de agosto al 22 de septiembre
# Libra                       del 23 de septiembre al 22 de octubre
# Escorpio                    del 23 de octubre al 21 de noviembre
# Sagitario                   del 22 de noviembre al 21 de diciembre

# Escriba un programa que le pida al usuario que ingrese su mes y día de nacimiento. 
# Entonces su programa debe informar el signo del zodiaco del usuario como parte de una salida adecuada mensaje.

mes = input('Ingrese su mes de nacimiento: ')
dia = input ('Ingrese el dia de nacimiento: ')


if (mes== 'diciembre' and dia >= '22') or (mes== 'enero' and dia <= '19'):
    print('Tu signo es capricornio')
elif (mes== 'enero' and dia >= '20') or (mes== 'febrero' and dia <= '10'):
    print('Tu signo es acuario')
elif (mes== 'febrero' and dia >= '19') or (mes== 'marzo' and dia <= '20'):
    print('Tu signo es piscis')
elif (mes== 'marzo' and dia >= '21') or (mes== 'abril' and dia <= '19'):
    print('Tu signo es aries')
elif (mes== 'abril' and dia >= '20') or (mes== 'mayo' and dia <= '20'):
    print('Tu signo es tauro')
elif (mes== 'mayo' and dia >= '21') or (mes== 'junio' and dia <= '20'):
    print('Tu signo es geminis')
elif (mes== 'junio' and dia >= '21') or (mes== 'julio' and dia <= '22'):
    print('Tu signo es cancer')
elif (mes== 'julio' and dia >= '23') or (mes== 'agosto' and dia <= '22'):
    print('Tu signo es leo')
elif (mes== 'agosto' and dia >= '23') or (mes== 'septiembre' and dia <= '22'):
    print('Tu signo es virgo')
elif (mes== 'septiembre' and dia >= '23') or (mes== 'octubre' and dia <= '22'):
    print('Tu signo es libra')
elif (mes== 'octubre' and dia >= '23') or (mes== 'noviembre' and dia <= '21'):
    print('Tu signo es escorpio')
elif (mes== 'noviembre' and dia >= '22') or (mes== 'diciembre' and dia <= '21'):
    print('Tu signo es sagitario')
else:
    
    print('\n ingresa la sintaxis: ')
    print('El mes en minuscula. Ejemplo: enero')
    print('El dia a dos digitos. Ejemplo: 06')