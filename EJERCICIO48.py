# Ejercicio 48

# Zodiaco chino.

# El zodiaco chino asigna animales a años en un ciclo de 12 años. Un ciclo de 12 años se muestra en la tabla a continuación.
# El patrón se repite a partir de ahí, con 2012 siendo otro año del dragón, y 1999 siendo otro año de la liebre.

#    Año                Animal
#    2000               Dragon
#    2001               Serpiente
#    2002               Caballo
#    2003               Ovejas
#    2004               Mono
#    2005               Gallo
#    2006               Perro
#    2007               Cerdo
#    2008               Rata
#    2009               Buey
#    2010               Tigre
#    2011               Liebre

# Escriba un programa que lea un año del usuario y muestre el animal asociado con ese año.
# Su programa debería funcionar correctamente durante cualquier año mayor o igual a cero, no solo los que figuran en la tabla.

año = int(input('Ingrese un año para ver el animal asociado a este año: '))

animal = ''

if año % 12 == 8:
    animal = 'Dragon'
elif año % 12 == 9:
    animal = 'Serpiente'
elif año % 12 == 10:
    animal = 'Caballo'
elif año % 12 == 11:
    animal = 'Ovejas'
elif año % 12 == 0 :
    animal = 'Mono'
elif año % 12 == 1:
    animal = 'Gallo'
elif año % 12 == 2:
    animal = 'Perro'
elif año % 12 == 3:
    animal = 'Cerdo'
elif año % 12 == 4:
    animal = 'Rata'
elif año % 12 == 5:
    animal = 'Buey'
elif año % 12 == 6:
    animal = 'Tigre'
elif año % 12 == 7:
    animal = 'Liebre'

print('', animal)