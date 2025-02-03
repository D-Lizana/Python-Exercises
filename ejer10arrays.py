# (L2) 6. Hacer un programa que lea 100 números aleatorios entre 0 y10 y genere un histograma con las frecuencias de cada numero.
#  Para representar las barras del histograma se utilizara secuencias ‘*’. Por ejemplo, la secuencia: 1, 1, 3, 4, 1, 3, 1, 2,...... generaría la siguiente salida:

import random

array = [None]*100

for i in range(100):
    array[i]=random.randint(1,10)

for i in range(1,11):
    print(f"{i}: ",end="")
    for j in range(100):
        if array[j]==i:
            print("*",end="")  
    print()          
