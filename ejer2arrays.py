# Rellenar un vector de 10 posiciones con valores del 1 al 100, para ello utiliza el método Math.random() * 101

import random

array = [None] * 10

for i in range(10):
    array[i] = random.randint(1,100)

print(array)