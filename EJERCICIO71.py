# EJERCICIO 71

# Raíz cuadrada.

# Escriba un programa que implemente el método de Newton para calcular y mostrar el cuadrado
# raíz de un número ingresado por el usuario. El algoritmo para el método de Newton sigue:
# Leer x del usuario
# Inicializar adivinar a x / 2
# Mientras que adivinar no es lo suficientemente bueno
# Actualizar conjetura para que sea el promedio de conjetura y x / conjetura
# Cuando se completa este algoritmo, supongo que contiene una aproximación del cuadrado
# raíz. La calidad de la aproximación depende de cómo se defina "lo suficientemente bueno".
# En la solución del autor, la conjetura se consideraba suficientemente buena cuando el valor absoluto
# de la diferencia entre adivinar ∗ adivinar y x fue menor o igual a 10−12.

import math
def main():
   

  x = eval(input("\n Introduzca la raiz cuadrada: "))
  conjetura = eval(input("¿Cuál es tu conjetura?: "))
  
  newt = (conjetura + (x / conjetura)) / 2 
  aprox = math.sqrt(x) - newt
  
  print("\n La raiz cuadra de ", x,"es: ", newt)
  print("la fórmula es", aprox,"precisa")

main()