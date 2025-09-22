
class Vulnerabilidad:
    def __init__(self, nombre, severidad, descripcion):
        
        severidades = ["Baja","Media","Alta","Crítica"]

        if severidad not in severidades:
            raise ValueError(f"Valor incorrecto, debe ser una de {severidades}")
        
        self.nombre = nombre
        self.severidad = severidad
        self.descripcion = descripcion

    def mostrar_info(self):
        print(self.nombre)
        print(self.severidad)
        print(self.descripcion)
    
    def recomendar_acciones(self):
        if self.severidad == "Crítica":
            recomendacion = "Aplicar parches de seguridad inmediatamente y revisar sistemas afectados."
        elif self.severidad == "Alta":
            recomendacion = "Realizar una auditoría de seguridad y aplicar medidas correctivas lo antes posible."
        elif self.severidad == "Media":
            recomendacion = "Monitorizar la actividad del sistema y planificar la aplicación de parches."
        elif self.severidad == "Baja":
            recomendacion = "Mantener bajo observación y revisar en el próximo ciclo de actualización."

        print(f"Acción recomendada: {recomendacion}")



v1 = Vulnerabilidad("SQL injection", "Alta", "Permite la ejecución de consultas SQL no autorizadas")
v2 = Vulnerabilidad("XSS", "Media", "Permite la ejecución de scripts en el navegador del usuario")
v3 = Vulnerabilidad("Desbordamiento Buffer", "Crítica", "Permite la ejecución arbitraria de código")


registro_vulnerabilidades = [v1,v2,v3]

for v in registro_vulnerabilidades:
    v.mostrar_info()
    v.recomendar_acciones()