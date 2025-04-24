# Desarrolla un programa que solicite al usuario los siguientes datos:
# 1. Capital inicial (monto principal).
# 2. Tasa de interés anual (en porcentaje).
# 3. Número de años.
# Con estos datos, el programa debe calcular:
# • El interés simple usando la fórmula:
# Interes = Capital * Tasa/ 100 * Años
# • El monto total acumulado (capital + interés).
# Finalmente, muestra ambos resultados. Si se ingresa algún valor negativo, muestra un
# mensaje de error y finaliza la operación.

try:
    capitalInicial = int(input("Introduce el capital inicial: "))
    interes = float(input("Introduce la tasa de interés anual (en porcentaje): "))
    tiempo = int(input("Introduce el número de años: "))

    if capitalInicial<0 or interes<0 or tiempo<0:
        raise ValueError

    interesSimple = float(capitalInicial * (interes/100) * tiempo)
    print(f"El interés simple es de {interesSimple:.02f} euros.")
    print(f"El monto total acumulado es de {capitalInicial+interesSimple:.02f}.")

except ValueError:
    print("No se pueden introducir números negativos.")
