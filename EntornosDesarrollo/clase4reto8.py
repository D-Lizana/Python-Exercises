# Implementa una función recursiva llamada suma_digitos que reciba un número entero y retorne la
# suma de sus dígitos. Por ejemplo, si se ingresa el número 1234, la función debe retornar 10 (1 + 2 +
# 3 + 4). Demuestra el funcionamiento de la función solicitando un número al usuario y mostrando el
# resultado de la suma de sus dígitos.

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        # con numero%10 aislamos el ultimo numero, y con numero//10 cogemos el resto y lo volvemos a pasar a suma_digitos
        return numero%10 + suma_digitos(numero//10)


def main():
    numero = int(input("Introduce un número: "))
    print(suma_digitos(numero))

main()