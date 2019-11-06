# Ejercicio 50

# Raíces de una función cuadrática.

# Una función cuadrática univariada tiene la forma f (x) = ax2 + bx + c, donde a, b y
# c son constantes y a no es cero. Se pueden encontrar las raíces de una función cuadrática
# encontrando los valores de x que satisfacen la ecuación cuadrática ax2 + bx + c = 0. A
# La función cuadrática puede tener 0, 1 o 2 raíces reales. Estas raíces se pueden calcular usando
# la fórmula cuadrática, que se muestra a continuación:
# raíz = −b ± √ b2 - 4ac
#            2a
# La parte de la expresión debajo del signo de raíz cuadrada se llama discriminante.
# Si el discriminante es negativo, entonces la ecuación cuadrática no tiene raíces reales.
# Si el discriminante es 0, entonces la ecuación tiene una raíz real. De lo contrario, la ecuación
# tiene dos raíces reales, y la expresión debe evaluarse dos veces, una vez usando un signo más
# signo, y una vez que usa un signo menos, al calcular el numerador.
# Escriba un programa que calcule las raíces reales de una función cuadrática. Su programa
# debe comenzar solicitando al usuario los valores de a, b y c. Entonces debería mostrar
# un mensaje que indica el número de raíces reales, junto con los valores de las raíces reales
# (Si alguna).

from math import sqrt

a = float(input("Ingresa un valor para a: "))
b = float(input("Ingresa un valor para b: "))
c = float(input("Ingresa un valor para c: "))

discriminante = (b**2) - (4*a*c)

if discriminante < 0:
	print("La ecuacion cuadrática no tiene raíces reales.")
elif discriminante == 0:
	print("Laecuacion cuadrática tiene una raíz real.")
	
	real = -b / 2*a 
	
	print('La raiz real es: ',real)
	
elif discriminante > 0:
	print("La ecuacion cuadrática tiene dos raíces reales.")
	
	real1 = (-b + (sqrt(discriminante))) / (2*a)
	real2 = (-b - (sqrt(discriminante))) / (2*a) 
	
	print('Las dos raices reales son: ', real1, '' , real2)
