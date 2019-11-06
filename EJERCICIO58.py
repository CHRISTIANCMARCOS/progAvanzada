# Ejercicio 58

# Día siguiente.

# Escriba un programa que lea una fecha del usuario y calcule su sucesor inmediato.
# Por ejemplo, si el usuario ingresa valores que representan 2013-11-18, entonces su programa
# debería mostrar un mensaje que indique que el día inmediatamente posterior al 2013-11-18 es
# 2013-11-19. Si el usuario ingresa valores que representan 2013-11-30, entonces el programa
# debe indicar que al día siguiente es 2013-12-01. Si el usuario ingresa valores que representan
# 31/12/2013, entonces el programa debe indicar que el día siguiente es 01-01-2014. los
# la fecha se ingresará en forma numérica con tres declaraciones de entrada separadas; uno para
# el año, uno para el mes y otro para el día. Asegúrese de que su programa funcione
# correctamente para los años bisiestos.

ano = int(input("Introduce el año: "))
mes = int(input("Introduce el mes: "))
dia = int(input("Introduce el dia: "))

siguienteano = ano
siguientemes = mes
siguientedia = dia

if mes != 12:
	siguienteano = ano 
else:
	if dia != 31:
		siguienteano = ano 
	else:
		siguienteano = ano + 1
		
# Sep, April, June, November only have 30 days

if mes != 9 and mes != 4 and mes != 6 and mes != 6 and mes != 11:
	if dia != 31:
		siguientemes = mes
		siguientedia = dia + 1
	else:
		if mes != 12:
			siguientemes = mes + 1
		else:
			siguientemes = 1
		siguientedia = 1
else:
	if dia != 30:
		siguientemes = mes 
		siguientedia = dia + 1
	else:
		if mes != 12:
			siguientemes = mes + 1
		else:
			siguientemes = 1
		siguientedia = 1
		
if mes != 2:
	bisiesto = True

	if ano % 400 == 0:
		bisiesto = True
	elif ano % 100 == 0 and not ano % 400 == 0:
		bisiesto = False 
	elif ano % 4 == 0 and not ano % 100 == 0 and not ano % 400 == 0:
		bisiesto = True 
	
	if dia == 28:
		if bisiesto:
			siguientemes = mes 
			siguientedia = dia + 1
		else :
			siguientemes = mes + 1
			siguientedia = 1
			
	else:
		siguientemes = mes 
		siguientedia = dia + 1
		
print("El siguiente dia es : ",siguienteano, '-', siguientemes,'-' ,siguientedia)