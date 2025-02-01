# 3. Hacer un programa que cree un array de 10 posiciones de números aleatorios entre 1 y 100.
#  Posteriormente se pedirá por teclado una posición y se mostrara en pantalla que valor tiene esa posición. (L1)

import random

array = [None]*10
for i in range(10):
    array[i] = random.randint(1,100)

print(array)

numero = int(input("Introduce un número entre el 1 y el 10: "))

print(f"El valor de esa posición es: {array[numero-1]}")