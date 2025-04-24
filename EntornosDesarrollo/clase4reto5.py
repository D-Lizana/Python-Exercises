# Diseña un programa que simule un sistema de autenticación simple. El programa debe:
# 1. Establecer una contraseña predefinida (por ejemplo, "python123").
# 2. Pedir al usuario que ingrese la contraseña.
# 3. Utilizar un bucle while para seguir solicitando la contraseña hasta que el usuario la ingrese
# correctamente.
# 4. Cuando se ingrese la contraseña correcta, imprimir "Acceso concedido" y el número de
# intentos realizados.

contrasenaPredefinida = "python123"
acceso = False
contador = 0

while(acceso==False):

    contrasena = input("Introduce contraseña: ")

    if contrasena == contrasenaPredefinida:
        acceso = True
        print("Acceso concedido.")
        print(f"Intentos realizados: {contador}")
    else:
        print("Contraseña incorrecta.")
        contador += 1
