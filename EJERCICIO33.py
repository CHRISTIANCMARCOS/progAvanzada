# Ejercicio 33

# Pan de un día.

# Una panadería vende hogazas de pan por $ 3.49 cada una. El pan de un día tiene un descuento de 60
# por ciento. Escriba un programa que comience leyendo la cantidad de panes de un día
# pan que se compra al usuario. Entonces su programa debe mostrar el regular
# precio del pan, el descuento porque tiene un día y el precio total. Toda la
# los valores deben mostrarse con dos decimales y los puntos decimales en todos
# de los números deben alinearse cuando el usuario ingresa valores razonables.

panundia = int(input('Ingrese la cantidad de panes en un dia: '))

pan = 3.49
descuento = 0.60

precioregular = pan * panundia
descuento = precioregular * descuento
total = precioregular - descuento

print ("El precio regular es:  %5.2f" % precioregular)
print ("El descuento es:       %5.2f" % descuento)
print ("El total es:           %5.2f" % total)