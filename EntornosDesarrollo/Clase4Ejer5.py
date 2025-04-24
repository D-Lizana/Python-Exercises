# 5. Bucles While
# Enunciado:
# 1.Utiliza un bucle while para pedir al usuario que introduzca números.
# 2.El programa deberá seguir pidiendo números mientras el número ingresado sea mayor o
# igual a cero.
# 3.Cuando el usuario introduzca un número negativo, el programa finaliza y muestra todos
# los números introducidos (puedes mostrarlos en una lista).

numeros = []
condicion = True

while(condicion):
    numero = int(input("Introduce un número entero: "))
    if numero>=0:
        numeros.append(numero)
    else:
        condicion = False

print(numeros)