# Ejercicio 56

# Bill de teléfono celular

# Un plan particular de telefonía celular incluye 50 minutos de tiempo al aire y 50 mensajes de texto.
# por $ 15.00 al mes. Cada minuto adicional de tiempo en el aire cuesta $ 0.25, mientras que adicional
# los mensajes de texto cuestan $ 0.15 cada uno. Todas las facturas de teléfonos celulares incluyen un cargo adicional de
# $ 0.44 para respaldar los centros de llamadas al 911, y la factura completa (incluido el cargo del 911) es
# sujeto al 5 por ciento de impuesto a las ventas.

# Escriba un programa que lea la cantidad de minutos y mensajes de texto utilizados en un
# mes del usuario. Muestra el cargo base, el cargo por minutos adicionales (si corresponde),
# cargo adicional por mensaje de texto (si corresponde), la tarifa 911, impuestos y el monto total de la factura. Solamente
# mostrar los cargos adicionales por minutos y mensajes de texto si el usuario incurrió en costos en
# Estas categorías. Asegúrese de que todos los cargos se muestren con 2 decimales.

minutos = int(input('Ingrese la cantidad de minutos de tiempo aire usados: '))
mensajes = int(input('Ingrese la cantidad de mensajes: '))

base = 15.00
print('Cargo base:  $', '%.2f' % base)

if minutos >50:
    min = minutos-50
    addmin = min *0.15
    print('Costo adicional por minutos: $', '%.2f' % addmin)
elif minutos:
    addmin = 0 


if mensajes >50:
    minu = mensajes-50
    addmen = minu * 0.25
    print('Costo adicional por mensajes: $' , '%.2f' % addmen)
elif mensajes:
    addmen = 0 


cargo = 0.44
print('Cargo del 911: $' , '%.2f' % cargo)

subtotal = base + addmin + addmen + cargo

impuesto = subtotal * 0.5
print('El impuesto es: $', '%.2f' % impuesto)

total = subtotal + impuesto
print('Total: $' '%.2f' % total)

