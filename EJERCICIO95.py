# EJERCICIO 95

# Matrícula Aleatoria

En una jurisdicción particular, las matrículas más antiguas constan de tres letras seguidas de
Tres números. Cuando se utilizaron todas las placas que siguen ese patrón,
El formato se cambió a cuatro números seguidos de tres letras.
Escriba una función que genere una matrícula aleatoria. Tu función debería tener
probabilidades aproximadamente iguales de generar una secuencia de caracteres para una licencia anterior
placa o una nueva placa de matrícula. Escriba un programa principal que llame a su función y
muestra la placa generada al azar.

import random as rand

def license_gen():
    set_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    set_numbers = [1,2,3,4,5,6,7,8,9,0]
    lenght = rand.randint(3,4)
    licen_numbs = rand.sample(set_numbers,lenght)
    licen_letts = rand.sample(set_letters,3)
    licen = ''
    if lenght == 3: 
        for i in licen_letts:
            licen = licen + i
        for i in licen_numbs: 
            licen = licen + str(i)
    elif lenght == 4: 
        for i in licen_numbs:
            licen = licen + str(i)
        for i in licen_letts: 
            licen = licen + i    
    print(licen)
    return licen

def main():
    license_gen()

main()