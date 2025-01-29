#  Rellenar un vector de 10 posiciones con valores introducidos por teclado. Deberá de mostrar los mensajes:
#  Introduce el numero 1º, Introduce el número 2º.... e Introduce el último número.
#  Posteriormente los mostrará todos por pantalla en una misma línea separado por guiones

array = [None]*10

for i in range(10):
    array[i] = int(input(f"Introduce el numero {i+1}: "))

for j in range(len(array)):
    print(f"{array[j]}", end="-")