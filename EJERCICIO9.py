# Ejercicio 9

# Interes compuesto.

# Usted acaba de abrir una nueva cuenta de ahorros con el cual gana el 4% de interes al año.
# El interes que usted genera es pagado al final del año, y es agregado al balance de la cuenta de banco.
# Escriba un programa que comiene por leer la cantidad de dinero depositada en la cuenta (el usuario introduce esta cantidad).
# El programa debe calcular y mostrar la cantidad de dinero en la cuenta despues del primer, segundo y tercer año.
# Despliegue las cantidades de dinero redondeando a dos decimales.


primeraño= float(input('\nInserte la cantidad de dinero a calcular los intereses: '))

año1= primeraño/100 * 4 + primeraño
año2= año1/100 * 4 + año1
año3= año2/100 * 4 + año2


print('\n\nEl balance de su cuenta seria')

print('\n Primer año: $', '%.2f' % año1)
print('\nSegundo año: $', '%.2f' % año2)
print('\n Tercer año: $', '%.2f' % año3)