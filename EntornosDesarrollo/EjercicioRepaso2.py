class Almacen():
    def __init__(self, localizacion, stock, empleados):
        self.localizacion = localizacion
        self.stock = stock
        self.empleados = empleados


    def mostrar_informacion(self):
        return f"{self.localizacion}, {self.stock}, {self.localizacion}"


class Tienda(Almacen):
    def __init__(self, localizacion, stock, empleados, facturacion):
        super().__init__(localizacion, stock, empleados)
        self.facturacion = facturacion
