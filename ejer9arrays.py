# 4. Hacer un programa que cree un array cuyo tamaño se pedirá por teclado y cuyo contenido serán números aleatorios entre 1 y 300.
# Posteriormente se creara otro array que guardara aquellos números del primer array que acaben en un dígito que se i ndicara por teclado
# (se debe controlar que se introduce un numero correcto). Finalmente, mostrar por pantalla los dos arrays. (L2). 

import random

tamano = int(input("Tamaño del array: "))

array = [None]*tamano

for i in range(len(array)):
    array[i] = random.randint(1,300)

print(array)

control = False
numero = 0

while not control:
    numero = int(input("Introduce un número del 0 al 9: "))
    if numero in range(10):
        control = True
    else:
        print("Número no válido.")

arrayDos = []

for i in range(len(array)):
    if array[i]%10 == numero:
        arrayDos.append(array[i])

print(arrayDos)