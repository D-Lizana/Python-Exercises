# Define una función lambda que convierta una distancia dada en kilómetros a millas (utilizando el
# factor de conversión: 1 kilómetro ≈ 0.621371 millas). Aplica esta lambda a cada elemento de la
# siguiente lista de distancias en kilómetros:
# • [5, 10, 15, 20, 25]
# Genera una nueva lista con las distancias convertidas a millas y muéstrala en pantalla.

kilometros_a_millas = lambda x: x*0.621371

distancias = [5,10,15,20,25]

distancia_en_millas = list(map(kilometros_a_millas, distancias))

print(distancia_en_millas)