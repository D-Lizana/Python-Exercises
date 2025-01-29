# (L2) 8. Escribe un programa que obtenga los números enteros comprendidos entre dos números introducidos por teclado y validados como distintos,
#  el programa debe empezar por el menor de los enteros introducidos e ir incrementando de 7 en 7. 

numeroUno = int(input("Primer numero: "))
numeroDos = int(input("Segundo numero: "))

if numeroUno != numeroDos:
    for i in range(numeroUno, numeroDos, 7):
        print(i)
else:
    print("Los numeros no pueden ser iguales")