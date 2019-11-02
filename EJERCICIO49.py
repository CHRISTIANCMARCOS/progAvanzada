# Ejercicio 49

# Eescala de richter. 

# La siguiente tabla contiene rangos de magnitud de terremotos en la escala de Richter y sus descriptores:


# Magnitud                 Descriptor
# Menos de 2.0             Micro
# 2.0 a menos de 3.0       Muy menor
# 3.0 a menos de 4.0       Menor
# 4.0 a menos de 5.0       Light
# 5.0 a menos de 6.0       Moderado
# 6.0 a menos de 7.0       Fuerte
# 7.0 a menos de 8.0       Mayor
# 8.0 a menos de 10.0      Genial
# 10.0 o más               Meteorico

# Escriba un programa que lea la admiración del usuario y muestre la información apropiada.
# descriptor como parte de un mensaje significativo. Por ejemplo, si el usuario ingresa 5.5 entonces
# su programa debe indicar que un terremoto de magnitud 5.5 se considera terremoto moderado

magnitud = input('Ingrese la magnitud: ')

if magnitud <= '1.9' and magnitud >= '0.0':
    print('Terremoto micro')
elif magnitud >= '2.0' and magnitud <= '2.9':
    print('Terremoto muy menor')
elif magnitud >= '3.0' and magnitud <= '3.9':
    print('Terremoto menor')
elif magnitud >= '4.0' and magnitud <= '4.9':
    print('Terremoto ligth')
elif magnitud >= '5.0' and (magnitud <= '5.9'):
    print('Terremoto moderado')
elif magnitud >= '6.0' and magnitud <= '6.9':
    print('Terremoto fuerte')
elif magnitud >= '7.0' and magnitud <= '7.9':
    print('Terremoto mayor')
elif magnitud >= '8.0' and magnitud <= '9.9':
    print('Terremoto genial')
elif magnitud >= '10.0' and magnitud <= '20.0':
    print('Terremoto muy meteorico')

