# OK (L1) 1. Pedir la edad a un usuario y decir que no puede pasar hasta que cumpla 18. 
paso = False

while not paso:
    edad = int(input("Cuantos años tienes? "))
    if edad >= 18:
        print("Puedes pasar.")
        paso = True
    else:
        print("Largo")