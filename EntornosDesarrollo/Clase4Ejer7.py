# 7. Funciones Lambda
# Enunciado:
# 1.Define una función lambda que reciba un número y lo multiplique por 10.
# 2.Aplica esa lambda a cada elemento de la lista [1, 2, 3, 4, 5] para generar una nueva lista.
# 3.Imprime la nueva lista resultante.

multiplicarx10 = lambda x: x*10

lista = [1,2,3,4,5]

nuevaLista = list(map(multiplicarx10, lista))

print(nuevaLista)

nuevaLista2 = [x*10 for x in nuevaLista]

print(nuevaLista2)