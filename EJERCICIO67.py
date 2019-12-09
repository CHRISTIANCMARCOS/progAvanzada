# EJERCICIO 67

# Precio de admisión.

# Un zoológico en particular determina el precio de admisión según la edad del huésped.
# Los huéspedes de 2 años de edad y menores son admitidos sin cargo. Niños entre 3 y
# 12 años de edad cuestan $ 14.00. Las personas mayores de 65 años y más cuestan $ 18.00. Admisión
# para todos los demás huéspedes es de $ 23.00.
# Cree un programa que comience leyendo las edades de todos los invitados en un grupo
# del usuario, con una edad ingresada en cada línea. El usuario ingresará una línea en blanco para
# indica que no hay más invitados en el grupo. Entonces su programa debería mostrar
# El costo de admisión para el grupo con un mensaje apropiado. El costo debe ser
# se muestra con dos decimales.

personas = int(input("¿Cuanta gente?: "))
costo = 0
conteo = 0

while conteo < personas:
  edad = int(input("¿Cuál es la edad ?: "))
  if edad <=12 and edad >=3:
    costo = costo + 14
  if edad >= 65:
    costo = costo + 18
  if edad >= 13 and edad <= 64:
    costo = costo + 23
  conteo = conteo + 1
  
  
print("El total es: $", costo)
