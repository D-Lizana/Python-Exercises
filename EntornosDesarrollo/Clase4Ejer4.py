# 4. Bucles For
# Enunciado:
# 1.Crea una lista de 5 números, por ejemplo: [5, 2, 7, 1, 9].
# 2.Utilizando un bucle for, recorre la lista y calcula la suma total de los elementos.
# 3.Imprime el resultado de la suma.

numeros = [5,2,7,1,9]
contador = 0

for i in range(len(numeros)):
    contador += numeros[i]

print(f"{contador}")