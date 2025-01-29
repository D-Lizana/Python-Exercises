# OK (L1) 8. Muestra la tabla de multiplicar de un número introducido por teclado. 

numero = int(input("Introduce un numero: "))

for i in range(10):
    print(f"{numero}*{i}={numero*i}")