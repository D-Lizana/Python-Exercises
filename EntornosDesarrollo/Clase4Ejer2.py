# 2. Programa de Ejemplo: Calculadora
# Enunciado:
# 1.Crea un programa que pida al usuario dos números enteros.
# 2.Muestra la multiplicación y la división entre ellos.
# 3.Si el divisor (segundo número) es 0, muestra un mensaje que indique que la división no
# es posible

numeros = input("Introduce dos numeros enteros separados por un espacio: ")

try:
    numero1, numero2 = numeros.split(" ")
    numero1 = int(numero1)
    numero2 = int(numero2)

    print(f"{numero1}*{numero2}={numero1*numero2}")
    print(f"{numero1}/{numero2}={numero1/numero2}")

except ZeroDivisionError:
    print("No es posible dividir entre 0")
