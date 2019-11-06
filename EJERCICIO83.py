# Ejercicio 83

# 

# Amaon provee envio epress para mucho de sus productos a un costo de 195 pesos por el pirmer producto 
# y de 29.50 para cada producto subsecuente. Escriba una funcion que tome el numero de productos como su unico argumento
# Regrese el costo de encio total como el resutado de la funcion, incluyaun programa principal que lea el numero de productos 
# comprados por el ususario y que despliegue el costo total de envio.

def envio(productos):
    if productos == 1:
        total = 195
    elif productos >= 2:
        total = 195 + (29.50 * (productos-1))
    return total

prod = int(input('Ingrese el numero de productos comprados: '))

precio = envio(prod)

print('El precio total de envio es: ', precio)

