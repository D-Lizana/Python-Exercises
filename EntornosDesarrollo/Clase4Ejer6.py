# 6. Funciones, Variables Locales y Globales
# Enunciado:
# 1.Define una función llamada cuadrado que reciba un número y retorne el cuadrado de
# ese número. Utiliza una variable local en la función.
# 2.Declara una variable global llamada mensaje_global y escribe otra función que la
# modifique.
# 3.Muestra por pantalla el resultado de la función cuadrado y el valor de la variable global
# tras la modificación.


def cuadrado(numero):
    return numero*numero

def modificar(mensaje):
    return "Tira de aquella"
    
def main():
    numero = int(input("Introduce un número: "))
    print(cuadrado(numero))
    mensaje_global = "Tira de esta"
    print(modificar(mensaje_global))


main()