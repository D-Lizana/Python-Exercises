#9. Realiza un programa que pinte una pirámide por pantalla. La altura se debe pedir por teclado. El carácter con el que se pinta la pirámide también se debe pedir por teclado.

altura = int(input("Introduce la altura de la piramide: "))
simbolo = input("Simbolo ")

for i in range(altura):
    for j in range(altura-1,-1):
        print(" ")
    for k in range((2*i)-1,1):
        print(f"{simbolo}")
