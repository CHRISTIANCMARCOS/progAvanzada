# EJERCICIO 96

# Verificar una contraseña.

# En este ejercicio escribirá una función que determina si una contraseña es o no
# es bueno. Definiremos una buena contraseña como una que tenga al menos 8 caracteres.
# largo y contiene al menos una letra mayúscula, al menos una letra minúscula y
# al menos un número Su función debe devolver verdadero si la contraseña se le pasó como
# Su único parámetro es bueno. De lo contrario, debería devolver falso. Incluir un programa principal
# que lee una contraseña del usuario e informa si es buena o no. Asegurar
# que su programa principal solo se ejecuta cuando su solución no se ha importado a
# otro archivo

def checkPassword(password): 
    has_upper = False
    has_lower = False
    has_num = False
    
    for ch in password: 
        if ch >= 'A' and ch <= 'Z': 
            has_upper = True
        elif ch >= 'a' and ch <= 'z': 
            has_lower = True
        elif ch >= '0' and ch <= '9':    
            has_num = True
    
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False

def main(): 
    p = input("Ingrese Contraseña: " )
    if checkPassword(p): 
        print("La contraseña es buena")
    else: 
        print("La contraseña es débil")

if __name__ == "__main__": 
    main()