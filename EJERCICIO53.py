# Ejercicio 53

# Evaluar empleados.

# En una empresa en particular, los empleados son calificados al final de cada año. La escala de calificación
# comienza en 0.0, con valores más altos que indican un mejor rendimiento y resultados más grandes
# plantea. El valor otorgado a un empleado es 0.0, 0.4 o 0.6 o más. Valores
# entre 0.0 y 0.4, y entre 0.4 y 0.6 nunca se usan. El significado asociado
# con cada calificación se muestra en la siguiente tabla. El monto del aumento de un empleado
# es $ 2400.00 multiplicado por su calificación.
# Valoración Significado

# 0.0 Rendimiento inaceptable
# 0.4 Rendimiento aceptable
# 0.6 o más rendimiento meritorio

# Escriba un programa que lea una calificación del usuario e indique si el rendimiento
# fue inaceptable, aceptable o meritorio. El monto del empleado
# aumento también debe ser reportado. Su programa debe mostrar un error apropiado
# mensaje si se ingresa una calificación no válida.

calificacion = float(input('Ingrese la calificacion del empleado: '))

if calificacion == 0.0:
    print('Rendimiento inaceptable')
elif calificacion == 0.4:
    print('Rendimiento aceptable')
elif calificacion >= 0.6:
    print('Rendimiento meritorio')
else:
    print('Calificacion no valida')


montoempleado = 2400 * calificacion
print('El monto del aumento del empleado es:', montoempleado)

