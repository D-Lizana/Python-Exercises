# 1. Hacer un programa que calcule la letra de un DNI. Se pedirá el DNI por teclado y devolverá el DNI la letra.
#  Para buscar la letra, se calcula el resto de dividir el dni entre 23, y con el resultado que estará entre 0 y 22,
#  se busca en el array de caracteres la letra correspondiente. El orden de los caracteres es: (L1)

letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

numeroDNI = int(input("Introduce número del DNI: "))

letraDNI = numeroDNI%23
letraDNI = letras[letraDNI]

print(f"{numeroDNI}{letraDNI}")
