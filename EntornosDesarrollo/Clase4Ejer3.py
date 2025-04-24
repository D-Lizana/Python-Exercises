# 3. Condicionales (if, elif, else)
# Enunciado:
# 1.Pide al usuario que introduzca una nota en una escala de 0 a 10.
# 2.Según la nota, muestra:
# Menor que 5: "Suspendido"
# Entre 5 y 6 (inclusive 5 y menor o igual a 6): "Aprobado"
# Entre 7 y 8: "Notable"
# Mayor que 8 hasta 10: "Sobresaliente"
# 3.Si la nota es menor que 0 o mayor que 10, muestra un mensaje indicando que la nota
# está fuera de rango.

nota = int(input("Introduce un número del 1 al 10: "))

if nota<0 or nota>10:
    print("La nota no es válida")
elif nota<5:
    print("Suspenso")
elif nota>=5 and nota<=6:
    print("Aprobado")
elif nota>=7 and nota<=8:
    print("Notable")
else:
    print("Sobresaliente")
