
class Empleado:

    # Constructor
    def __init__(self, id_empleado, nombre, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self-salario = salario

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
        self-salario = salario
        self.departamento = departamento

    def aprobar_proyecto(self):
        print(f"Gerente {self.nombre} del departamento {self.departamento} aprueba el proyecto.")

