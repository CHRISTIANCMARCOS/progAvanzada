# EJERCICIO 64

# No más centavos.

# El 4 de febrero de 2013 fue el último día en que el Royal Canadian distribuyó centavos.
# Menta. Ahora que los centavos se han eliminado, los minoristas deben ajustar los totales para que puedan
# son múltiplos de 5 centavos cuando se pagan en efectivo (tarjeta de crédito y débito)
# las transacciones se siguen cargando al centavo). Mientras que los minoristas tienen algo de libertad
# en cómo lo hacen, la mayoría elige redondear al níquel más cercano.
# Escriba un programa que lea los precios del usuario hasta que se ingrese una línea en blanco.
# Muestra el costo total de todos los artículos ingresados ​​en una línea, seguido del monto
# debido si el cliente paga con efectivo en una segunda línea. El monto adeudado por un efectivo
# el pago debe redondearse al níquel más cercano. Una forma de calcular el efectivo
# el monto del pago comenzará determinando cuántos centavos serían necesarios para
# pagar el total Luego calcule el resto cuando este número de centavos se divide
# por 5. Finalmente, ajuste el total hacia abajo si el resto es inferior a 2.5. De lo contrario, ajuste el total arriba.

suma = 0
sumaredondeada = 0

interrumpido = False 
while not interrumpido:
	precio = input("Introduce el precio: ")
	
	if precio != "":
		precio = float(precio)
	else:
		break
		
	suma += precio 
	
	penique = precio * 100
	recorda = penique % 5
	
	if recorda > 2.5:
		penique +- 5 - recorda 
	else:
		penique -= recorda 
	
	redondeado = penique * 0.01
	sumaredondeada += redondeado

print("El costo actual es: %.2f" %(suma))
print("Pagando en efectivo: %.1f" %(sumaredondeada))