# EJERCICIO 87

# Centrar una cadena en la terminal.

# Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de
# el terminal en caracteres como su segundo parámetro. Su función debería devolver un nuevo
# cadena que consta de la cadena original y el número correcto de espacios iniciales
# para que la cadena original aparezca centrada dentro del ancho proporcionado cuando está
# impreso. No agregue ningún carácter al final de la cadena. Incluir un programa principal
# eso demuestra tu función.

WIDTH = 80

def centro(s, width):
    if width < len(s):
        return s
    
    espacios = (width - len(s)) // 2
    resultado = ' ' * espacios + s

    return resultado

def main():
    print(centro(' Es mecatronica', WIDTH))
    print(centro('para todos ', WIDTH))
    print(centro('un muy buena carrera', WIDTH))
    print()
    print('Por siempre...')
main()