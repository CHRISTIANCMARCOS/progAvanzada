# Ejercicio 32

# Ordenar 3 enteros

# Cree un programa que lea tres enteros del usuario y los muestre ordenados
# orden (de menor a mayor). Usa las funciones min y max para encontrar el más pequeño
# y valores más grandes. El valor medio se puede encontrar calculando la suma de los tres
# valores, y luego restando el valor mínimo y el valor máximo.

ent1 = int(input('Escriba el primer numero entero: '))
ent2 = int(input('Escriba el segundo numero entero: '))
ent3 = int(input('Escriba el tercer numero entero: '))

menor = min(ent1, ent2, ent3)
mayor = max(ent1, ent2, ent3)
medio = (ent1 + ent2 + ent3) - menor - mayor

print('El orden de menor a mayor es: ',menor, ',' ,medio, ',' ,mayor)

