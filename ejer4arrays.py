# Utiliza uno de los vectores anteriores y multiplícalo entero por un número introducido por el usuario

import random

array = [None] * 10
numero = int(input("Introduce numero: "))

for i in range(10):
    array[i] = random.randint(1,100)
    array[i] = array[i]%13
    array[i] = array[i]*numero


print(array)