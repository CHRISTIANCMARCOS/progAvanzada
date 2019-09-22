# Ejercicio 8.

# Cajas de cereal

# Un vendedor de una pagina de abarrotes en linea vende dos tipos de caja de cereal. CornFlakes
# de 750 gr y Trix de 500 gr. Escriba un programa que lea el numero de cajas de CornFlakes y 
# cajas de Trix cuyo valor debe ser introducido por el usuario. Despues, su programa debe calcular 
# y mostrar el total del peso (en kilogramos) del envio.

# CornFlakes= 750 gr
# Trix = 500 gr

cornkilogramo= 750/1000
trixkilogramo= 500/1000

Cor= int(input('\n\nInserte el numero de cajas de CornFlakes: '))
Tri= int(input('\nInserte el numero de cajas de Trix: '))

pesoCorn= cornkilogramo * Cor
pesoTrix= trixkilogramo * Tri

sumapeso= pesoCorn + pesoTrix

print('\n\nEl peso total es: ',sumapeso,'kg')
