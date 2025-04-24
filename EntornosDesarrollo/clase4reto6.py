# Crea un programa que realice lo siguiente:
# 1. Define una función llamada celsius_a_kelvin que reciba una temperatura en grados
# Celsius y retorne el valor en Kelvin, usando la fórmula:
# Kelvin=Celsius+273.15
# Utiliza una variable local para almacenar el resultado antes de retornarlo.
# 2. Declara una variable global llamada conteo_conversiones inicializada en 0.
# 3. Define una segunda función llamada convertir_temperatura que:
# • Reciba una temperatura en Celsius.
# • Llame a celsius_a_kelvin para obtener el valor en Kelvin.
# • Aumente en 1 el valor de conteo_conversiones.
# • Retorne el valor en Kelvin.
# 4. Pide al usuario una temperatura en Celsius, llama a convertir_temperatura y muestra
# el resultado en Kelvin junto con el total de conversiones realizadas (valor de
# conteo_conversiones).

conteo_conversiones = 0

def celsius_a_kelvin(celsius):
    kelvin=float(celsius+273.15)
    return kelvin

def convertir_temperatura(celsius):
    global conteo_conversiones
    kelvin = celsius_a_kelvin(celsius)
    conteo_conversiones += 1
    return kelvin

def main():
    celsius = float(input("Intruce temperatura en grados Celsius: "))
    kelvin = convertir_temperatura(celsius)
    print(f"La temperatura en grados Kelvin es: {kelvin}\nConversiones realizadas: {conteo_conversiones}")

main()