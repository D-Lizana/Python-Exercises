# 2. Hacer un programa que rellene un array con los 100 primeros números enteros y los muestre en pantalla en orden inverso a como se han introducido (orden inverso). (L1)

array = []

for i in range(100):
    array.append(i)

for i in range(99,-1,-1):
    print(f"{array[i]} ",end="")

