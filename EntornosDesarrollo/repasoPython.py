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
