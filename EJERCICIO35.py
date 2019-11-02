# Ejercicio 35

# Años de perro.

# Se dice comúnmente que un año humano es equivalente a 7 años de perro. 
# Sin embargo esto la conversión simple no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años.
# Como resultado, algunas personas creen que es mejor contar cada uno de los dos primeros años humanos como 10.5 años de perro, 
# y luego cuente cada año humano adicional como 4 perros años.

# Escribir un programa que implemente la conversión de años humanos a años de perros, descrito en el párrafo anterior.
# Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones
# de dos o más humanos años.
# Su programa debe mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.

humano = int(input('Ingresar la edad del perro en humano: '))

if humano <= 2:
    perro = humano * 10.5
elif humano > 2:
    perro = 2 * 10.5
    perro += (humano-2) * 4

if humano <= 0:
    print('Ingrese un numero entero.')

else:
   
    print('La edad del perro es: ', (perro))



