# OK (L2) 11. Escribe un programa que calcule la media de un conjunto de números positivos introducidos por teclado.
#  A priori, el programa no sabe cuántos números se introducirán. El usuario indicará que ha terminado de introducir los datos cuando meta un número negativo. 

contador = 0
sumador = 0
numero = 0

while numero >= 0:
    
    numero = int(input("Introduce un numero: "))
    if numero >= 0:
        sumador+=numero
        contador+=1

print(f"Media = {sumador/contador}")
