
class Empleado:

    # Constructor
    def __init__(self, id_empleado, nombre, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario = salario

    # Metodo
    def calcular_bonificacion(self):
        return self.salario * 0.1
    
    # toString
    def mostrar_informacion(self):
        info = f"id_empleado : {self.id_empleado}, nombre : {self.nombre}, salario : {self.salario}"
        return info
    

class Gerente(Empleado):
    def __init__(self, id_empleado, nombre, salario, departamento):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def aprobar_proyecto(self):
        print(f"Gerente {self.nombre} del departamento {self.departamento} aprueba el proyecto.")

class Departamento:
    def __init__(self, id_departamento, nombre):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado.mostrar_informacion())


def main():
    empleado1 = Empleado(1, "Diego", 50000)
    gerente1 = Gerente(2, "Javi", 60000, "Ciberseguridad")

    departamento1 = Departamento(66, "Ciberseguridad")

    departamento1.agregar_empleado(gerente1)
    departamento1.agregar_empleado(empleado1)

    departamento1.mostrar_empleados()

if __name__ == "__main__":
    main()
    