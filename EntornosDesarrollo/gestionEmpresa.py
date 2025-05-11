class Empleado():
    def __init__(self,id_empleado,nombre,salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario = salario

    def calcular_bonificaciones(self):
        self.salario = self.salario + (self.salario * 0.1)

    def mostrar_informacion(self):
        info = f"id_empleado : {self.id_empleado}, nombre : {self.nombre}, salario : {self.salario}."
        return info

class Gerente(Empleado):
    def __init__(self, id_empleado, nombre, salario, departamento):
        super().__init__(id_empleado, nombre, salario)
        self.departamento = departamento

    def aprobar_proyecto(self):
        print(f"El gerente {self.nombre} del departamento {self.departamento} ha aprobado el proyecto.")


    
class Departamento():
    def __init__(self, id_departamento, nombre):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.empleados = []