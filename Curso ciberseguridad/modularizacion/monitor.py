
def verificar_disponibilidad(hosts):
    resultados = {}
    for host in hosts:
        if host.startswith("192"):
            resultados[host] = "Disponible"
        else:
            resultados[host] = "No disponible"

    return resultados
            