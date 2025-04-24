# 8. Recursividad (Factorial)
# Enunciado:
# 1.Define una función recursiva factorial(n) que calcule y retorne el factorial del número n.
# 2.Recuerda que el factorial de 0 es 1 y para n > 0, se cumple que:
# factorial(n) = n * factorial(n - 1)
# 3.Demuestra el funcionamiento de la función llamándola, por ejemplo, con n = 5.


def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

def main():
    numero = int(input("Introduce un número: "))
    print(factorial(numero))

main()