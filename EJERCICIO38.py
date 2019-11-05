# Ejercicio 38 

# Nombre del mes a la cantidad de días.

# La duración de un mes varía de 28 a 31 días. En este ejercicio crearás un programa que lee el nombre de un mes del usuario como una cadena. 
# Entonces el programa debe mostrar la cantidad de días en ese mes. Mostrar "28 o 29 días" para febrero para que se aborden los años bisiestos.

mes = input('Ingrese el mes para ver su duración: ')

tre = 'abril,junio,septiembre,noviembre' 
vein = 'febrero'

if mes in vein:
    print('Este mes dura aveces 28 o 29 dias')
elif mes in tre:
    print('Este mes dura 30 dias')
else:
    print('Este mes dura 31 dias')
  