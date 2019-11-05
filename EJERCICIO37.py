# Ejercicio 37

# Nombra esa forma.

# Escriba un programa que determine el nombre de una forma a partir de su número de lados.
# Leer el número de lados del usuario y luego informa el nombre apropiado como parte de un mensaje significativo. 
# Su programa debe admitir formas con 3 hasta (e incluyendo) 10 lados. 
# Si se ingresa un número de lados fuera de este rango entonces su programa debería mostrar un mensaje de error apropiado.

lados = int(input('Inserte el numero de lados para ver el nombre de la figura: '))

if lados == 3:
    print ('Es un triangulo')
elif lados == 4:
    print ('Es un cuadrado')
elif lados == 5:
    print ('Es un pentagono')
elif lados == 6:
    print ('Es un hexagono')
elif lados == 7:
    print ('Es un heptagono')
elif lados == 8:
    print ('Es un octagono')
elif lados == 9:
    print ('Es un nonagono')
elif lados == 10:
    print ('Es un decagono')
else:
    print ('Ingrese un valor >= a 3 o <= a 10')


