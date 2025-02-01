# Utiliza uno de los vectores anteriores y almacena en ese mismo vector el resto de la división de cada número por 13

import random

array = [None] * 10

for i in range(10):
    array[i] = random.randint(1,100)
    array[i] = array[i]%13

print(array)