#EJERCICIO 6.

# Impuestos y propina

# Hacer un programa en el que el usuario introduca el nombre de la comida que ordeno en un restaurante
# y su precio, despues su programa debe calcular el subtotal, el iva y la propina de toda la cuenta.
# La salida del programa debe parecerce a tiket de restaurante use un iva del 16% y una propina del 15% del subtotal.
# Los valores numericos deben tener dos decimales. 


comida1= (input('\nIntroduzca el nombre de la comida; '))
precio1=float(input('Introduzca el valor de la comida; '))
comida2= (input('\nIntroduzca el nombre de la comida; '))
precio2=float(input('Introduzca el valor de la comida; '))
comida3= (input('\nIntroduzca el nombre de la comida; '))
precio3=float(input('Introduzca el valor de la comida; '))
comida4= (input('\nIntroduzca el nombre de la comida; '))
precio4=float(input('Introduzca el valor de la comida; '))
comida5= (input('\nIntroduzca el nombre de la comida; '))
precio5=float(input('Introduzca el valor de la comida; '))

subtotal= precio1 + precio2 + precio3 + precio4 + precio5
iva= subtotal / 100 * 16
propina= subtotal / 100 * 15
total= subtotal + iva + propina



print('\n\n\n\n\n subtotal: $', '%.2f' % subtotal)
print('                iva: $', '%.2f' % iva)
print('            propina: $', '%.2f' % propina)
print('------------------------')
print('             total:  $', '%.2f' % total)