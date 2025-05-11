
vuelos = ["V01","V02","V03","V04","V05"]
destinos = ["Madrid", "Osaka", "Budapest", "Vilna", "Edimburgo"]
exit = False

while exit==False:
    pregunta = input("Dime el numero de vuelo o salir (exit): ")

    if pregunta == "exit":
        exit = True
        print("Has salido del programa.")

    elif pregunta.upper() not in vuelos:
        print("El vuelo indicado no existe.")

    else:
        for i in range(len(vuelos)):
            if pregunta.upper() == vuelos[i]:
                print(destinos[i])

    