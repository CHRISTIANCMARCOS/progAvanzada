# Ejercicio 55

# Frecuencia para nombrar

# La radiación electromagnética se puede clasificar en una de las 7 categorías según su
# frecuencia, como se muestra en la tabla a continuación:

# Nombre                 Rango de frecuencia (Hz)
# Ondas de radio         Menos de 3 × 109
# Microondas             3 × 109 a menos de 3 × 1012
# Luz infrarroja         3 × 1012 a menos de 4.3 × 1014
# Luz visible            4.3 × 1014 a menos de 7.5 × 1014
# Luz ultravioleta       7.5 × 1014 a menos de 3 × 1017
# Rayos X                3 × 1017 a menos de 3 × 1019
# Rayos gamma            3 × 1019 o más

# Escriba un programa que lea la frecuencia de la radiación del usuario y muestre
# El nombre apropiado.

frecuencia = float(input('Ingrese la frecuencia de la radiacion: '))

if frecuencia < 3e9:
    print('Ondas de radio')
elif frecuencia >= 3e9 and frecuencia < 3e12:
    print('Microondas')
elif frecuencia >= 3e12 and frecuencia < 4.3e14:
    print('Luz infrarroja')
elif frecuencia >= 4.3e14 and frecuencia < 7.5e14:
    print('Luz visible')
elif frecuencia >= 7.5e14 and frecuencia < 3e17:
    print('Luz ultravioleta')
elif frecuencia >= 3e17 and frecuencia < 3e19:
    print('Rayos X')
elif frecuencia >= 3e19:
    print('Rayos gamma')


