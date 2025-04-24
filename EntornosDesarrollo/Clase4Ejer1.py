# 1. Input, Output y Variables
# Enunciado:
# 1.Pide al usuario que introduzca su nombre y su altura en centímetros.
# 2.Imprime un mensaje en el siguiente formato:
# "Hola [nombre], mides [altura] cm"
# 3.Convierte la altura a metros (1 metro = 100 cm) y vuelve a imprimir un mensaje en el
# siguiente formato:
# "Hola [nombre], mides [altura_en_metros] metros"

nombre = input("Introduce nombre: ")
altura = int(input("Introduce altura en cm: "))

print(f"Hola {nombre}, mides {altura}cm.")

altura = float(altura/100)

print(f"Hola {nombre}, mides {altura} metros.")