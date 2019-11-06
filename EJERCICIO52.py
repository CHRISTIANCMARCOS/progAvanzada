# Ejercicio 52

# Calificación de puntos a calificación de letras

# En el ejercicio anterior, creó un programa que convierte una calificación de letra en
# número equivalente de puntos de calificación. En este ejercicio creará un programa que
# invierte el proceso y convierte de un valor de punto de calificación introducido por el usuario a un
# grado de la letra. Asegúrese de que su programa maneje los valores de calificación que se encuentran entre
# Grados de letras. Estos deben redondearse al grado de letra más cercano. Su programa
# debe reportar A + para un promedio de calificaciones de 4.0 (o más).

puntos = float(input("Inserte la califiacion en puntos: "))

grado = ""

if puntos >= 4.0 and puntos <= 10.0:
	grado = "A+"
elif puntos >= 3.85 and puntos < 4.0:
	grado = "A"
elif puntos >= 3.5 and puntos < 3.85:
	grado = "A-"
elif puntos >= 3.15 and puntos < 3.5:
	grado = "B+"
elif puntos >= 2.85 and puntos < 3.15:
	grado = "B"
elif puntos >= 2.5 and puntos < 2.85:
	grado = "B-"
elif puntos >= 2.15 and puntos < 2.5:
	grado = "C+"
elif puntos >= 1.85 and puntos < 2.15:
	grado = "C"
elif puntos >= 1.5 and puntos < 1.85:
	grado = "C-"
elif puntos >= 1.15 and puntos < 1.5:
	grado = "D+"
elif puntos >= 0.5 and puntos < 1.15:
	grado = "D"
elif puntos >= 0 and puntos < 0.5:
	grado = "F"


if grado != "":
	print('Tu calificacion es: ', grado)
else:
	print('Puntos no validos.')