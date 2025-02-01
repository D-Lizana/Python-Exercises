# Utiliza uno de los vectores anteriores y calcula la media con los números que contiene

import random

array = [None] * 10
numero = int(input("Introduce numero: "))
sumador = 0

for i in range(10):
    array[i] = random.randint(1,100)
    array[i] = array[i]%13
    array[i] = array[i]*numero
    sumador+=array[i]

media = sumador/len(array)

print(media)