# EJERCICIO 17

# Capacidad calorífica.

# La cantidad de energía requerida para aumentar la temperatura de un gramo de material
# en un grado Celsius es la capacidad de calor específica del material, C. La cantidad total
# de energía requerida para elevar m gramos de un material en ΔT grados Celsius puede ser
# calculado usando la fórmula:

# q = mCΔT.

# Escriba un programa que lea la masa de un poco de agua y el cambio de temperatura
# del usuario. Su programa debe mostrar la cantidad total de energía que debe ser
# agregado o eliminado para lograr el cambio de temperatura deseado.

# Sugerencia: La capacidad calorífica específica del agua es 4.186 J/g◦C. 
# Porque el agua tiene una densidad de 1.0 gramo por mililitro, puede usar gramos y mililitros indistintamente en este ejercicio.

# Extienda su programa para que también calcule el costo de calentar el agua. 
# Electricidad normalmente se factura utilizando unidades de kilovatios hora en lugar de julios. 
# En esto ejercicio, debe suponer que la electricidad cuesta 8.9 centavos por kilovatio-hora. 
# Utilizar su programa para calcular el costo de hervir agua por una taza de café.

# Sugerencia: deberá buscar el factor para convertir entre julios y kilovatios hora para completar la última parte de este ejercicio.

capcaloragua = 4.186
julio = 2.77778e-7


volumen = float(input('Ingresar la cantidad de agua en mililitros: '))
tempincrementa = float(input('Ingresa la temperatura que incrementa: '))
 
q = volumen * capcaloragua * tempincrementa

print('La cantidad de energia que debe ser agregado o eliminado es: ', q, 'Joules')

kilovatiosh = q * julio

print('la cantidad en kilowatios - hora es: ', '%.02f' % kilovatiosh)

precio = 8.9

precio1 = kilovatiosh * precio

print('El precio para hervir agua es: ', '%.02f' % precio1, 'centavos')


