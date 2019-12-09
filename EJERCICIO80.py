# EJERCICIO 80

# Coin Flip Simulation.

# ¿Cuál es el número mínimo de veces que tiene que lanzar una moneda antes de poder tener
# tres lanzamientos consecutivos que resultan en el mismo resultado (los tres son cara o
# los tres son colas)? ¿Cuál es el número máximo de volteos que podrían ser necesarios? Cómo
# cuántas vueltas se necesitan en promedio? En este ejercicio exploraremos estas preguntas
# creando un programa que simule varias series de lanzamientos de monedas.
# Cree un programa que use el generador de números aleatorios de Python para simular el volteo
# una moneda varias veces La moneda simulada debe ser justa, lo que significa que la probabilidad
# de caras es igual a la probabilidad de colas. Tu programa debe voltearse simulado
# monedas hasta que ocurran 3 caras consecutivas de 3 colas consecutivas. Mostrar una H cada
# cada vez que el resultado es cara y una T cada vez que el resultado es cruz, con todos los
# resultados mostrados en la misma línea. Luego muestre la cantidad de vueltas necesarias para alcanzar
# 3 lanzamientos consecutivos con el mismo resultado. Cuando se ejecuta su programa, debería
# realice la simulación 10 veces e informe el número promedio de vueltas necesarias.

import random



def coin_flipper():
    
    opcion = ['S', 'C']
    vueltas = ''
    
    while True:
        vuelta = random.choice(opcion)
        vueltas = vueltas + vuelta
        
        if len(vueltas) >= 3:
            if ( vueltas[-3] == vueltas[-2] == vueltas[-1] ):
                break
            else:
                continue
    return vueltas




resultado = []
suma = 0

for i in range(10):
    resultado.append(coin_flipper())
    suma += len(resultado[i])
    print(resultado[i], "(%d)" %len(resultado[i]))

vueltasprom = suma/10    

print ("En promedio %d vueltas" %vueltasprom)