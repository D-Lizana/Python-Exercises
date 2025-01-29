# (L2) 1. Escribe un programa que muestre en tres columnas, el cuadrado y el cubo de los 5 primeros números enteros a partir de uno que se introduce por teclado. 

numero = int(input("Introduce numero: "))

for i in range(5):
    cuadrado = numero*numero
    cubo = numero*numero*numero
    print(f"{numero} / {cuadrado} / {cubo}")
    numero+=1