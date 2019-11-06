# Ejercicio 81

#

# Escribir una funcion que tome la longitud de los dos lados mas cortos de un triangulo rectangulo como argumentos.
# La funcion debe de regresar la hipotenusa del triangulo calculado utiliando el teorema de pitagoras como el resultado de la funcion.
# Incluya un programa principal que lea las longitudes de los lados mas cortos del triangulo rectangulo insertados por el 
# usuario, usando la funcion para calcular la longitud de la hipotenusa y qie tambien se despliegue el resultado.

def calcular_hipotenusa(lado1, lado2):

    hipotenusa = (lado1**2 + lado2**2)**(0.5)

    return hipotenusa

L1 = float(input('Inserta el valor del lado 1: '))
L2 = float(input('Inserta el valor del lado 2: '))

hip = calcular_hipotenusa(L1,L2)

print('La hipotenusa es: ',hip)

