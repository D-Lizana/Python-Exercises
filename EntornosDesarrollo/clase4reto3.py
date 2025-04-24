# Escribe un programa que pida al usuario su edad y, utilizando estructuras condicionales, clasifique
# la edad según las siguientes categorías:
# • Menor de 12 años: "Niñez".
# • Entre 12 y 17 años: "Adolescencia".
# • Entre 18 y 64 años: "Adultez".
# • 65 años o más: "Tercera edad".
# Si el usuario ingresa un número negativo, el programa debe mostrar un mensaje que indique
# que la edad es inválida.

try:
    edad = int(input("Introduce tu edad: "))

    if edad<0:
        print("No puede ser un número negativo.")
    elif edad<12:
        print("Niñez.")
    elif edad>=12 and edad<=17:
        print("Adolescencia.")
    elif edad>=18 and edad<= 64:
        print("Adultez.")
    else:
        print("Tercerda edad.")

except ValueError:
    print("Introduce un número.")