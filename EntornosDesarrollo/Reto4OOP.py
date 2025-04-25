class Soldado:
    def __init__(self,nombre,peso,altura):
        self.nombre = nombre

        try:
            self.peso = int(peso)
            self.altura = int(altura)
        except ValueError:
            print("El peso y el nombre tienen que ser números.")

        self.fuerza = int(100)
        self.estado = "Vivo"

    def perdida(self, valor):
        if self.estado == "Muerto":
            print(f"{self.nombre} ya está muerto.")
        else:
            print(f"{self.nombre} ha recibido un herida de {valor}.")
            self.fuerza -= valor
            if self.fuerza <= 0:
                self.estado = "Muerto"
                print(f"{self.nombre} ha muerto.")
            else:
                print(f"La fuerda de {self.nombre} es {self.fuerza}.")

    def ganancia(self, valor):
        if self.estado == "Muerto":
            print(f"{self.nombre} está muerto. No puede curarse.")
        else:
            print(f"{self.nombre} se ha curado {valor}.")
            self.fuerza += valor

            if self.fuerza > 100:
                self.fuerza = 100
                print(f"La fuerza de {self.nombre} es {self.fuerza}.")
            else:
                print(f"La fuerza de {self.nombre} es {self.fuerza}.")

def main():
    henry = Soldado("Henry",75,175)
    
    
    henry.perdida(50)
    henry.perdida(30)
    henry.ganancia(5)
    henry.ganancia(120)
    henry.perdida(100)
    henry.ganancia(20)

if __name__ == "__main__":
    main()
