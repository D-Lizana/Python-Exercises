# Crea un programa que contenga una lista predefinida de colores, por ejemplo:
# • ["rojo", "verde", "azul", "amarillo"]
# El programa debe:
# 1. Pedir al usuario que ingrese un índice numérico para seleccionar un color de la lista.
# 2. Utilizar bloques try/except para manejar posibles errores:
# • Errores al convertir la entrada a entero (ValueError).
# • Errores al acceder a un índice fuera de los límites de la lista (IndexError).
# 3. En cualquier caso, usar un bloque finally para imprimir un mensaje indicando que la
# operación ha finalizado.
# 4. Si la selección es exitosa, mostrar el color correspondiente.

colores = ["rojo","verde","azul","amarillo"]

try:
    numero = int(input("Introduce un número: "))
    print(f"El color seleccionado es: {colores[numero]}")

except ValueError:
    print("Número no válido.")

except IndexError:
    print("La lista no tiene tantos valores.")

finally:
    print("Fin del bloque try/except.")