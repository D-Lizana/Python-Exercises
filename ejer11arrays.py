# (L1) 1. Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, el primero que se introduce es el último en mostrarse y viceversa.

array = [None]*10

for i in range(10):
    array[i] = input("Introduce número: ")

for i in range(9,-1,-1):
    print(f"{array[i]} ",end="")
