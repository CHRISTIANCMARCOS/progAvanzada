# EJERCICIO 88

# ¿Es un triángulo válido?.

# Si tiene 3 pajitas, posiblemente de diferentes longitudes, puede o no ser posible
# acostarlos para que formen un triángulo cuando sus extremos se toquen. por
# ejemplo, si todas las pajitas tienen una longitud de 6 pulgadas. entonces uno puede construir fácilmente
# un triángulo equilátero usándolos. Sin embargo, si un popote es de 6 pulgadas. largo, mientras que el
# las otras dos son cada una de solo 2 pulgadas. largo, entonces no se puede formar un triángulo. En general,
# si alguna longitud es mayor o igual que la suma de las otras dos, entonces las longitudes
# no se puede usar para formar un triángulo. De lo contrario, pueden formar un triángulo.
# Escribe una función que determine si tres longitudes pueden o no formar un triángulo.
# La función tomará 3 parámetros y devolverá un resultado booleano. Además, escribe un
# programa que lee 3 longitudes del usuario y demuestra el comportamiento de este
# función.

def triangle(a, b, c): 
    lenghts = [a,b,c]
    lenghts.sort()
    if lenghts[2] < (lenghts[1] + lenghts[0]):
        return True
    else: 
        return False

lado_a = float(input("Ingrese lado a: "))
lado_b = float(input("Ingrese lado b: "))
lado_c = float(input("Ingrese lado c: "))

if triangle(lado_a, lado_b, lado_c): 
    print("Es posible construir un triángulo")
else: 
    print("No es posible construir un triángulo")