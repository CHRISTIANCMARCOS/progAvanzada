# Ejercicio 13

# Haciendo el cambio.

# Considere el software que se ejecuta en una máquina de autopago. 
# Una tarea que debe ser capaz de realizar es determinar cuánto cambio proporcionar cuando el comprador paga para una compra en efectivo.
# Escriba un programa que comience leyendo una cantidad de centavos del usuario como entero.
# Luego, su programa debe calcular y mostrar las denominaciones de monedas que deberían usarse para dar esa cantidad de cambio al comprador. 
# El cambio debe administrarse utilizando la menor cantidad de monedas posible.
# Suponga que la máquina está cargada con centavos, monedas de cinco centavos, monedas de diez centavos, cuartos, locos y toonies.

# Una moneda de un dólar se introdujo en Canadá en 1987. Se conoce como Loonie porque un lado de la moneda tiene un loon (un tipo de pájaro).
# Los dos la moneda de un dólar, conocida como toonie, se introdujo 9 años después. 
# Su nombre es derivado de la combinación del número dos y el nombre del loco.

centavos= int(input('Introduzca la cantidad de centavos: '))

toonies = 200
locos = 100
m1cuar = 25
m10 = 10
m5 = 5


centavos1 = centavos // toonies
centavos11 = centavos % toonies
print('', centavos1, 'toonies')
centavos2 = centavos11 // locos
centavos22 = centavos11 % locos
print('', centavos2, 'locos')
centavos3 = centavos22 // m1cuar
centavos33 = centavos22 % m1cuar
print('', centavos3, 'monedas de un cuarto')
centavos4 = centavos33 // m10
centavos44 = centavos33 % m10
print('', centavos4, 'monedas de diez')
centavos5 = centavos44 // m5
centavos55 = centavos44 % m5
print('', centavos5, 'monedas de cinco')
print('', centavos55, 'centavo')



