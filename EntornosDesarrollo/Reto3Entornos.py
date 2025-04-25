# Se necesita un programa que haga una operación matemática (por ejemplo 37 + 12).  
# Características: 
#   • El programa se seguirá ejecutando hasta que yo de la respuesta 
# correcta.   
#   • Si fallo el programa me debe decir si me he pasado o me he quedado 
# corto. 
#   • Puedo introducir por pantalla los dos números que quiero que se 
# sumen, por lo tanto, la suma ya no es siempre la misma, si no la que el 
# usuario elija.   
#   • Controlar los posibles errores.

try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    solucion = False

    while(solucion==False):
        resultado = float(input(f"Resuelve la suma {numero1}+{numero2}="))

        if resultado == (numero1+numero2):
            print("Resultado correcto.")
            solucion = True
        else:
            print("Resultado incorrecto.")
            if resultado < (numero1+numero2):
                print("Te has quedado corto.")
            elif resultado > (numero1+numero2):
                print("Te has pasado.")

except ValueError:
    print("Número no válido")

finally:
    print("Operacion terminada.")