# Crea un programa que solicite al usuario su ciudad de residencia y el número aproximado de
# habitantes de esa ciudad. Luego, imprime el siguiente mensaje:
# • "La ciudad de [ciudad] tiene aproximadamente [habitantes] habitantes."
# A continuación, convierte el número de habitantes a miles (dividiendo entre 1000) y
# muestra:
# • "Esto equivale a [habitantes_en_miles] mil habitantes."

ciudad = input("Introduce el nombre de tu ciudad: ")
habitantes = int(input(f"Introduce el número aproximado de habitantes de {ciudad}: "))

print(f"La ciudad de {ciudad} tiene aproximadamente {habitantes} habitantes.")

habitantes = int(habitantes/1000)

print(f"Esto equivale a {habitantes} mil habitantes.")