contraseña = input("Introduce contraseña: ")

def validar_contrasena(contraseña):
    if len(contraseña) < 8:
        raise ValueError("corta")
    if not any(c.islower() for c in contraseña):
        raise ValueError("Minusculas")
    if not any(c.isupper() for c in contraseña):
        raise ValueError("Mayusculas")
    if not any(c in "@#$%&" for c in contraseña):
        raise ValueError("Simbolos")
    if not any(c.isdigit() for c in contraseña):
        raise ValueError("Numeros")
    
    
    return True
    
try:
    validar_contrasena(contraseña)

except ValueError as error:
    print(error)