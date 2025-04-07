frase = input("Introduce una frase: ").lower().replace(" ","")
palindromo = True

for i in range(len(frase)//2):
    if frase[i] != frase[len(frase)-i-1]:
        palindromo = False
        break

if palindromo == False:
    print("La frase no es un palíndromo.")
else:
    print("La frase es un palíndromo.")