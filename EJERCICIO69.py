# Ejercicio 69

# π aproximado.

# El valor de π se puede aproximar mediante las siguientes series infinitas:

# Escriba un programa que muestre 15 aproximaciones de π. La primera aproximación
# debe utilizar solo el primer término de la serie infinita. Cada aproximación adicional
# mostrado por su programa debe incluir un término más en la serie, haciendo
# es una mejor aproximación de π que cualquiera de las aproximaciones mostradas anteriormente.

i = 1
j = 0
suma = 0.0
signo = -1
while i <= 15:
    den = (i+1.0)*(i+2.0)*(i+3.0)
    signo = signo * -1
    suma = suma + (signo * 4.0) / den
    i = j + 2.0 
    pi_apro = 3.0 + suma
    j = j + 1
    print('interaccion: ', j, 'Pi apross', pi_apro)

