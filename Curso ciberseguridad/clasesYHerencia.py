
class Dispositivo:
    def __init__(self,nombre,ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.interfaces = []

    def mostrar_info(self):
        print(f"Dispositivo: {self.nombre}, Ubicación: {self.ubicacion}")
        for interfaz in self.interfaces:
            print(f"- Interfaz: {interfaz.nombre}, IP: {interfaz.ip}")

    def anadir_interfaz(self,interfaz):
        self.interfaces.append(interfaz)


class Interfaz:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip
    

class Router(Dispositivo):
    def __init__(self, nombre, ubicacion, modelo):
        super().__init__(nombre, ubicacion)
        self.modelo = modelo

class Switch(Dispositivo):
    def __init__(self, nombre, ubicacion, tipo):
        super().__init__(nombre, ubicacion)
        self.tipo = tipo


r1 = Router("Router1", "Data Center", "Cisco 2901")

i1 = Interfaz("GigabitEthernet0/0","192.168.1.1")
i2 = Interfaz("GigabitEthernet0/1","192.168.2.1")

r1.anadir_interfaz(i1)
r1.anadir_interfaz(i2)

r2 = Switch("Switch1","Oficina Principal","Capa 3")

i3 = Interfaz("FastEthernet0/1","192.168.1.2")
i4 = Interfaz("FastEthernet0/2","192.168.1.3")

r2.anadir_interfaz(i3)
r2.anadir_interfaz(i4)

r1.mostrar_info()
r2.mostrar_info()