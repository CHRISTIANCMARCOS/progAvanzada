# Ejercicio 40

# Nombra ese triángulo.

# Un triángulo se puede clasificar en función de la longitud de sus lados como isósceles equiláteros o escaleno.
# Los 3 lados de un triángulo equilátero tienen la misma longitud.
# Un isósceles el triángulo tiene dos lados que tienen la misma longitud y un tercer lado que es diferente longitud. 
# Si todos los lados tienen diferentes longitudes, entonces el triángulo es escaleno.
# Escriba un programa que lea las longitudes de 3 lados de un triángulo del usuario.
# Muestra un mensaje que indica el tipo de triángulo.

luno = float(input('Ingrese el valor del primer lado: '))
ldos = float(input('Ingrese el valor del segundo lado: '))
ltres = float(input('Ingrese el valor del tercer lado: '))

if luno == ldos == ltres:
    print('Es un triangulo equilatero')
elif luno == ldos or luno == ltres or ldos == ltres:
    print('Es un triangulo isoceles')
elif luno != ldos != ltres:
    print('Es un triangulo escaleno')


