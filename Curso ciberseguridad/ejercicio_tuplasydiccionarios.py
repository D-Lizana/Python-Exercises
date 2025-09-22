


platos = ["Paella","Risotto","Sushi", "Tacos", "Pizza"]
precios = [15,12,20,10,8]

platos_seleccionados = platos[1:3]

menu = {
    platos[0]:precios[0],
    platos[1]:precios[1],
    platos[2]:precios[2],
    platos[3]:precios[3],
    platos[4]:precios[4]
}

print(menu[platos[2]])

platos_pares = platos[1::2]
print(platos_pares)