# Ejercicio 39 

# Niveles de sonido

# La siguiente tabla enumera el nivel de sonido en decibelios para varios ruidos comunes.

#    Ruido                                 Decibel level (dB)
#    Martillo neumático                          130
#    Cortacésped a gas                           106
#    Despertador                                 70
#    Cuarto tranquilo                            40

# Escriba un programa que lea un nivel de sonido en decibelios del usuario. 
# Si el usuario ingresa un nivel de decibelios que coincide con uno de los ruidos en la tabla y luego su programa
# debería mostrar un mensaje que contenga solo ese ruido. Si el usuario ingresa un número de decibelios entre los ruidos enumerados, 
# entonces su programa debería mostrar un mensaje indicando entre qué ruidos se encuentra el nivel.
# Asegúrese de que su programa también genere salida razonable para un valor más pequeño que el ruido más bajo en la tabla,
# y para un valor mayor que el ruido más alto en la tabla.

db = float(input('Ingrese un valo de nivel de decibel(dB): '))

if db < 40:
    print('Nivel muy bajo de ruido')
elif db == 40:
    print('Cuarto tranquilo')
elif db > 40 and db < 70:
    print('Se encuentra entre cuarto tranquilo y despertador')
elif db == 70:
    print('Despertador')
elif db > 70 and db < 106:
    print('se encuentra entre despertador y cortacesped a gas')
elif db == 106:
    print('Cortacesped a gas')
elif db > 106 and db < 130:
    print('Se encuentra entre cortacesped a gas y martillo neumatico')
elif db == 130:
    print('Martillo neumatico')
else:
    print('Muy escandaloso e insoportable')