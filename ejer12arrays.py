# (L1) 2. Define tres arrays de 20 números enteros cada una, con nombres número, cuadrado y cubo.
#  Carga el array numero con valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el array número.
#  En el array cubo se deben almacenar los cubos de los valores que hay en número. A continuación, muestra el contenido de los tres arrays dispuesto en tres columnas.

import random

numero = [None]*20
cuadrado = [None]*20
cubo = [None]*20

for i in range(len(numero)):
    numero[i]=random.randint(1,100)
    cuadrado[i]=numero[i]*numero[i]
    cubo[i]=numero[i]**3
    print(f"{numero[i]} || {cuadrado[i]} || {cubo[i]}")

