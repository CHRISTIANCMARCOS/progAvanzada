# EJERCICIO 63

# Tabla de conversión de temperatura.

# Escriba un programa que muestre una tabla de conversión de temperatura para grados Celsius y grados Fahrenheit. 
# La tabla debe incluir filas para todas las temperaturas entre 0 y 100 grados centígrados que son múltiplos de 10 grados centígrados. 
# Incluir apropiado encabezados en sus columnas. 
# La fórmula para convertir entre grados Celsius y grados Fahrenheit se pueden encontrar en internet.

temp = input("Inserte la temperatura a convertir? (Ejemplo, 45F, 102C.) : ")
grados = int(temp[:-1])
i_conv = temp[-1]

if i_conv.upper() == "C":
  result = int(round((9 * grados) / 5 + 32))
  o_conver = "Fahrenheit"
elif i_conv.upper() == "F":
  result = int(round((grados - 32) * 5 / 9))
  o_conver = "Celsius"
else:
  print("Valor no valido.")
  quit()
print("Tu temperatura es:", o_conver, "es", result, "grados.")