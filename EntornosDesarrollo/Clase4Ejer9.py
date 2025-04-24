# 9. Manejo de Errores (try/except)
# Enunciado:
# 1.Pide al usuario que introduzca un número entero.
# 2.Divide 10 entre ese número.
# 3.Utiliza bloques try/except para manejar:
# El error al convertir el dato a entero.
# El error de división por cero.
# 4.Asegúrate de incluir un bloque finally que imprima un mensaje final, indicando que se
# ha finalizado la operación.


try:
    numero = int(input("Introduce un número entero: "))
    numero = 10/numero
    print(numero)

except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("No válido")

finally:
    print("Se ha acabado la operación")