# EJERCICIO 70

# Cifrado César.

# Uno de los primeros ejemplos de encriptacion fue usado por julio cesar, que necesitaba el enviarinstrucciones
# escritas a sus generales, pero el no queria que sus enemigos conocieran de sus planes en caso de que el mensaje 
# fuese interceptado. Como resuñltado el desarrollo lo que despues seria conocido como el cifrado de cesar. 
# La idea detras de este cifrado es simple (y como resultado, no tiene proteccion contra las tecnicas modernas
# de hackeo). Cada letra en el mensaje original se mueve tres lugares. Como resultado a se convierte en d,
# b se convierte en e, c se convierte en f, d se convierte en g, etc. Las ultimas tres letras del alfabeto 
# se mueven al inicio, es decir  se convierte en a, y se convierte en b y seta se convierte en c.
 
# Escriba un programa que implemente el cifrado cesar. Permita que el usuario inserte el mensaje y la cantidad
# de espacios a moverse, y despues despliegue el mensaje movido. Su programa debe de soportar letras 
# mayusculas y minusculas, su programa tambien debe soportar movientos con valores negativos de tal manera 
# que los mensajes se puedan cifrar y decifrar

frase = input('Introduce el mensaje a cifrar: ')
movimiento = int(input('Introduce cantidad a espacios a mover: '))

nfrase = ''

for ch in frase:
    if ch >= 'a' and ch <='z':
        pos = ord(ch) - ord('a')
        pos = (pos + movimiento) % 26
        caracter = chr (pos + ord ('a'))
        nfrase = nfrase + caracter
    elif ch >'A' and ch <= 'Z':
        pos = ord(ch) - ord ('A')
        pos = (pos + movimiento) % 26
        caracter = chr(pos + ord('A'))
        nfrase = nfrase + caracter
    else:
        nfrase = nfrase + ch
print('El mensaje cifrado es: ', nfrase)
