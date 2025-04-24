# Define una lista que contenga los nombres de 6 animales (por ejemplo, ["perro", "gato", "elefante",
# "jirafa", "tigre", "conejo"]). Utilizando un bucle for:
# 1. Recorre la lista y convierte cada nombre a mayúsculas antes de imprimirlo, precedido de su
# posición en la lista (por ejemplo, "1. PERRO").
# 2. Al final, calcula y muestra el total de caracteres de todos los nombres combinados.

animales = ["perro","gato","elefante","jirafa","tigre","conejo"]

for i in range(len(animales)):
    print(f"{i+1}. {animales[i].upper()}")
