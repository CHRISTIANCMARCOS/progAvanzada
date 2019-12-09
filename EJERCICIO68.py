# EJERCICIO 68

# Bits de paridad.

# Un bit de paridad es un mecanismo simple para detectar errores en los datos transmitidos a través de un
# conexión poco confiable como una línea telefónica. La idea básica es que un poco más
# se transmite después de cada grupo de 8 bits para que un solo error de bit en la transmisión
# puede ser detectado
# Los bits de paridad se pueden calcular para paridad par o paridad impar. Si incluso paridad
# se selecciona entonces el bit de paridad que se transmite se elige de modo que el número total
# de un bit transmitido (8 bits de datos más el bit de paridad) es par. Cuando paridad impar
# se selecciona el bit de paridad se elige de modo que el número total de un bit transmitido
# es impar.
# Escriba un programa que calcule el bit de paridad para grupos de 8 bits ingresados ​​por
# usuario usando paridad par. Su programa debe leer cadenas que contengan 8 bits hasta que
# El usuario ingresa una línea en blanco. Después de que el usuario ingrese cada cadena, su programa debería
# muestra un mensaje claro que indica si el bit de paridad debe ser 0 o 1. Pantalla
# un mensaje de error apropiado si el usuario ingresa algo diferente a 8 bits.

# Sugerencia: debe leer la entrada del usuario como una cadena. Entonces puedes usar
# El método de conteo para ayudarlo a determinar la cantidad de ceros y unos en el
# cuerda. La información sobre el método de conteo está disponible en línea.

def get_input():
  bits = input("Bits: ")
  return bits
  
def division(bits):
  num = bits.count("1")
  if num % 2 == 0:
    paridad = 0
  else:
    paridad = 1
  return paridad
  
def print_paridad(paridad):
  print("Bit de paridad: ", paridad)
  
def main():
  bits = get_input()
  if bits != "":
    paridad = division(bits)
    print_paridad(paridad)
  else:
    return True

while True:  
  linea_blanco = main()
  if linea_blanco == True:
    break
  
  