# Ejercicio 27.

# Índice de masa corporal

# Escriba un programa que calcule el índice de masa corporal (IMC) de un individuo. 
# Tu programa debe comenzar leyendo una altura y un peso del usuario. 
# Entonces debería usar una de las siguientes dos fórmulas para calcular el IMC antes de mostrarlo. 
# Si lees la altura en pulgadas y el peso en libras, entonces el índice de masa corporal es calculado usando la siguiente fórmula:

# IMC = ( weigth /eighth * eigth ) * 703


# Si lee la altura en metros y el peso en kilogramos, entonces el índice de masa corporal
# se calcula utilizando esta fórmula ligeramente más simple:

# IMC = ( weigth /height * height )

altura = float(input('Ingrese su altura en metros: '))
peso = float(input('Ingrese su peso en kg: '))

IMC = (peso ) / (altura * altura)
 
print ('Su Indice de Masa Corporal es: ','%.02f' % IMC)


