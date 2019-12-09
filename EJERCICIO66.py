# EJERCICIO 66

# Calcular un promedio de calificaciones.

# El ejercicio 51 incluyó una tabla que muestra la conversión de calificaciones de letras a calificaciones
# puntos en una institución académica particular. En este ejercicio calcularás el
# promedio de calificaciones de un número arbitrario de calificaciones de letras ingresadas por el usuario. los
# el usuario ingresará una línea en blanco para indicar que se han proporcionado todas las calificaciones. por
# ejemplo, si el usuario ingresa A, seguido de C +, seguido de B, seguido de un espacio en blanco
# línea, entonces su programa debe reportar un promedio de calificaciones de 3.1.
# Puede encontrar útil su solución para el ejercicio 51 al completar este ejercicio.
# Su programa no necesita hacer ninguna comprobación de errores. Puede suponer que cada valor
# ingresado por el usuario siempre será una calificación de letra válida o una línea en blanco.

conteo = 0
print("Este programa calculará su promedio de calificaciones. Ingrese calificaciones como A+, A, A-, B+, B, B-, C+,C,C-, D+, D-, F")
numero = int(input("¿Cuántas calificaciones te gustaría ingresar?: "))
totalpuntos = 0
while conteo < numero:
  grade = input("Ingrese su calificación: ")
  if grade == "A+":
    totalpuntos += 4.0
  if grade == "A":
    totalpuntos += 4.0
  if grade == "A-":
    totalpuntos += 3.7
  if grade == "B+":
    totalpuntos += 3.3
  if grade == "B":
    totalpuntos += 3.0
  if grade == "B-":
    totalpuntos += 2.7
  if grade == "C+":
    totalpuntos += 2.3
  if grade == "C":
    totalpuntos += 2.0
  if grade == "C-":
    totalpuntos += 1.7
  if grade == "D+":
    totalpuntos += 1.3
  if grade == "D":
    totalpuntos += 1.0
  if grade == "F":
    totalpuntos += 0.0
  conteo = conteo + 1

prom = totalpuntos/numero
print("Su promedio es:",prom)