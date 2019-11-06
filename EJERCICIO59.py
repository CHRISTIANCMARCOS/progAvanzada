# Ejercicio 59

# ¿Es válida una matrícula?.

# En una jurisdicción particular, las matrículas antiguas consisten en tres letras mayúsculas
# seguido de tres números. Cuando todas las placas que siguieron ese patrón tenían

# utilizado, el formato se cambió a cuatro números seguidos por tres mayúsculas
# letras.
# Escriba un programa que comience leyendo una cadena de caracteres del usuario. Entonces
# su programa debe mostrar un mensaje que indique si los caracteres son válidos
# para una placa de estilo anterior o una placa de estilo más nueva. Su programa debe
# mostrar un mensaje apropiado si la cadena ingresada por el usuario no es válida para
# Estilo de matrícula.


matricula = input("Introduce la matricula: ")

estilo = ""

if matricula[0] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[1] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[2] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
	if matricula[3] in "0123456789" and matricula[4] in "0123456789" and matricula[5] in "0123456789":
		estilo = "viejo"

elif matricula[0] in "0123456789" and matricula[1] in "0123456789" and matricula[2] in "0123456789" and matricula[3] in "0123456789":
	if matricula[4] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[5] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[6] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
		estilo = "nuevo"
		
if estilo == "viejo":
	print("Esta es una placa de estilo antiguo.")
elif estilo == "nuevo":
	print("Esta es una placa de estilo nuevo.")
else:
	print("Matrícula no válida ingresada.")
