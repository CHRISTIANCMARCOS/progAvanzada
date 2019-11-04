# Ejercicio 31

# Suma de los dígitos en un entero.

# Desarrolle un programa que lea un número entero de cuatro dígitos del usuario y muestre la suma
# de los dígitos en el número. Por ejemplo, si el usuario ingresa 3141, entonces su programa
# debería mostrar 3 + 1 + 4 + 1 = 9.

dig = int(input('Inserte un numero entero de cuatro digitos: '))

uno = dig // 1000
dos = dig % 1000
tres = dos // 100
tresu = dos % 100
cuatro = tresu // 10
cinco = tresu % 10

total = uno + tres + cuatro + cinco 

print('La suma de los digitos es: ')
print('',uno, ' + ' ,tres,' + ',cuatro,' + ',cinco, ' = ', total)

