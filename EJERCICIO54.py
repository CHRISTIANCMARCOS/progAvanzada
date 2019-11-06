# Ejercicio 54

# Longitudes de onda de luz visible.

# La longitud de onda de la luz visible varía de 380 a 750 nanómetros (nm). Mientras que la
# El espectro es continuo, a menudo se divide en 6 colores como se muestra a continuación:

# Longitud de onda de color (nm)
# Violeta        380 a menos de 450
# Azul           450 a menos de 495
# Verde          495 a menos de 570
# Amarillo       570 a menos de 590
# Naranja        590 a menos de 620
# Rojo           620 a 750

# Escriba un programa que lea la longitud de onda del usuario e informe su color. Monitor
# un mensaje de error apropiado si la longitud de onda ingresada por el usuario está fuera de
# espectro visible.

longdeonda = int(input('Ingrese un valor de longitud de onda: '))

if longdeonda >= 380 and longdeonda < 450:
    print('Color violeta')
elif longdeonda >= 450 and longdeonda < 495:
    print('Color azul')
elif longdeonda >= 495 and longdeonda < 570:
    print('Color verde')
elif longdeonda >= 570 and longdeonda < 590:
    print('Color amarillo')
elif longdeonda >= 590 and longdeonda < 620:
    print('Color naranja')
elif longdeonda >= 620 and longdeonda <= 750:
    print('Color rojo')
else:
    print('Longitud de onda esta fuera del espectro visible')

