# Ejercicio 30.

# Unidades de presión

# En este ejercicio creará un programa que lee la presión del usuario en kilopascales.
# Una vez que se ha leído la presión, su programa debe informar el equivalente
# presión en libras por pulgada cuadrada, milímetros de mercurio y atmósferas. Utilizar
# sus habilidades de investigación para determinar los factores de conversión entre estas unidades.

# 1 kpa = 0.145038 libras por pulgada cuadrada
# 1 kpa = 7.50062 milimetros de mercurio
# 1 kpa = 0.00986923 atmosferas 

presion = float(input('Ingrese la presion en kilopascales: '))

lpc = (presion * 0.145038)
mm = (presion * 7.50062)
atm = (presion * 0.00986923)

print('El equivalente en libras por pulgada cuadrada es: ', '%.02f' % lpc)
print('El equivalente en milimetros de mercurio es: ', '%.02f' % mm)
print('El equivalente en atmosferas es: ', '%.02f' % atm)

