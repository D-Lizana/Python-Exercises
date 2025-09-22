
from monitor import verificar_disponibilidad

hosts = ["192.168.1.1","192.168.1.2", "10.0.0.1"]

resultados = verificar_disponibilidad(hosts)

# Importante el resultados.items para desempaquetar los datos del diccionario
for host, estado in resultados.items():
    print(f"Host: {host}, Disponibilidad: {estado}")