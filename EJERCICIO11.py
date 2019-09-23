# EJERCICIO 11.

# Eficicencia de combustible

# En los Estados Unidos, la eficiencia del combustible para vehículos normalmente se expresa en millas por galón.
# En México, la eficiencia del combustible normalmente se expresa en litros por cien kilómetros (L / 100 km).
# Usa tus habilidades de investigación para determinar cómo convertir de MPG a L / 100 km.
# Luego cree un programa que lea un valor del usuario en América unidades y muestra la eficiencia de 
# combustible equivalente en unidades Mexicanas.

#Eficiencia 

# EUA= mpg
# Mexico= L/100 km

# Conversion 1mpg = 235.21 l /100 km

EUA= float(input('Ingrese el valor de la eficiencia en millas por galon a convertir: '))

con= EUA * 235.21

print('\n\nEl valor de la eficiencia en unidades mexicanas es:', '%.2f ' 'L /100 km' %  con )

