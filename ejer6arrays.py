# Utiliza uno de los vectores anteriores y dime cuál es el valor más alto y el más bajo

import random

array = [None] * 10
sumador = 0
minimo = 1000
maximo = 0 


for i in range(10):
    array[i] = random.randint(1,100)
    array[i] = array[i]%13
    if array[i] > maximo:
        maximo = array[i]
    if array[i] < minimo:
        minimo = array[i]

print(array)
print(minimo)
print(maximo)
