def ejercicio1():
    ciudad = input("Introduce ciudad: ")
    numero = int(input("Introduce número de habitantes: "))

    print(f"La ciudad de {ciudad} tiene {numero} habitantes.")
    print(f"Esto equivale a {numero/1000} mil habitantes.")


def ejercicio2():
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))

    try: 
        resultado = numero1 / numero2
        print(resultado)

    except ZeroDivisionError:
        print("No se puedee dividir entre 0")


def ejercicio3():
    nota = int(input("Introduce una nota entre 0 y 10: "))

    if nota < 0 or nota > 10:
        print("Nota no válida.")
    else:
        if nota < 5:
            print("Suspenso.")
        elif nota > 5 and nota <= 6:
            print("Aprobado.")
        elif nota >=7 and nota <=8:
            print("Notable.")
        else:
            print("Sobresaliente.")


def ejercicio4():
    numeros = [1,2,3,4,5]
    suma = 0

    for i in len(numeros-1):
        suma += i

    print(suma)


def ejercicio5():

    numero = 0
    numeros = []

    while numero >= 0:
        numero = int(input("Introduce número: "))
        numeros.append(numero)

    print(numeros)


mensaje_global = ""
def ejercicio6():

    def cuadrado(numero):
        return numero*numero

    def modificar():
        global mensaje_global
        mensaje_global = "Adios"
        return mensaje_global

    print(f"{cuadrado(2)}, {modificar()}")


def ejercicio7():
    funcion = lambda x: x*10
    numeros = [1,2,3,4,5]
    nueva_lista = list(map(funcion, numeros))

    print(nueva_lista)



def main():
    ejercicio7()

main()