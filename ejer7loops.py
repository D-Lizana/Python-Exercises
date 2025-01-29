# (L2) 2. Escribe un programa que muestre, cuente y sume los múltiplos de 3 que hay entre 1 y un número leído por teclado. 

contador = 0
sumador = 0

numero = int(input("Introduce numero: "))

for i in range(1,numero):
    if i%3 == 0:
        print(i)
        sumador+=i
        contador+=1

print(f"Contador: {contador}, sumador: {sumador}")
