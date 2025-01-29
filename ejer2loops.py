# OK (L1) 2. Crear un programa que juegue con el usuario a adivinar un número.
#  El programa generará un número aleatorio del 1 al 10 y el usuario introducirá números hasta adivinarlo.
#  Al final del programa se mostrará el número de intentos que ha tenido.

import random

contador = int(0)
adivina = False
numero = random.randint(1,10)

while not adivina:
    pregunta = int(input("Adivina el número: "))

    if pregunta == numero:
        contador+=1
        print(f"Correcto! Numero de intentos: {contador}")
        adivina = True
    else:
        contador+=1
        print("Numero incorrecto")