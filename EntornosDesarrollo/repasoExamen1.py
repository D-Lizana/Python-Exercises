def ejercicio1():
    ciudad = input("Introduce ciudad: ")
    habitantes = int(input("Introduce numero de habitantes: "))
    print(f"{ciudad} tiene aproximadamente {habitantes} habitantes.")

    habitantes = float(habitantes /1000)
    print(f"Esto equivale a {habitantes} mil habitantes")


def ejercicio2():
    capital = int(input("Introduce capital inicial: "))
    tasa = int(input("Introduce tasa de interés anual: "))
    tiempo = int(input("Introduce el número de años: "))

    if capital<0 or tasa<0 or tiempo<0:
        print("Los valores no pueden ser negativos.")

    else:
        interes = float(capital*(tasa/100)*tiempo)
        print(f"El interés simple es: {interes}")

        total = capital + interes

        print(f"El monto total acumulado es {total}.")


def ejercicio3():
    edad = int(input("Introduce edad: "))
    if edad <12:
        print("Niñez.")
    elif edad>=12 and edad<=17:
        print("Adolescencia.")
    elif edad>=18 and edad<=64:
        print("Adultez")
    else:
        print("Tercera edad.")


def ejercicio4():

    animales = ["perro","gato","elefante","jirafa","tigre","conejo"]
    sumador = 0

    for i in range(len(animales)):
        print(f"{i+1}. {animales[i]}")
        for j in range(len(animales[i])):
            sumador += 1

    print(f"El total de letras es {sumador}")


def ejercicio5():
    password = "python123"
    correcto = False

    while correcto==False:
        solicitud = input("Introduce contraseña: ")
        if solicitud==password:
            print("Contraseña correcta.")
            correcto = True
        else:
            print("Contraseña incorrecta.")

    print("Acesso concedido.")

def ejercicio6():
    numero1 = int(input("Introduce numero 1: "))
    numero2 = int(input("Introduce numero 2: "))

    try:
        resultado = numero1 / numero2
        print(f"{resultado}")
        if resultado == 1:
            raise Exception
        

    except (ZeroDivisionError):
        print("No se puede dividir entre 0")
    except (Exception):
        print("Tira de esta")

def ejercicio7():
    funcionLambda = lambda x: x*10
    lista = [1,2,3,4,5]
    listax10 = list(map(funcionLambda, lista))
    print(listax10)

def ejercicio8():
    f = lambda a,b: a*b
    print(f(3,4))

def main():
   ejercicio8()

main()