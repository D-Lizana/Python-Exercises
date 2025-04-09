class Libro:
    def __init__(self, isbn, titulo, anno_publicacion):
        self.isbn = isbn
        self.titulo = titulo
        self.anno_publicacion = anno_publicacion
        self.autores = []
        self.estado = "Disponible"

    def prestarLibro(self):
        if self.estado == "Disponible":
            self.estado = "Prestado"
            print(f"Se ha prestado el libro: {self.titulo}")
        else:
            print(f"El libro {self.titulo} no stá disponible.")
        
    def devolverLibro(self):
        if self.estado == "Prestado":
            self.estado = "Disponible"
            print(f"Se ha devuelto el libro: {self.titulo}.")

    def agregarAutor(self, autor):
        if autor not in self.autores:
            self.autores.append(autor)


    #Para poder mostrar libros cuando estén en la biblioteca
    def mostrarLibro(self):
        info = f"isbn : {self.isbn}, titulo : {self.titulo}, año de publicacion : {self.anno_publicacion}, autores : {self.autores}, estado : {self.estado}"
        return info
    



class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    def agregarLibros(self, libro):
        if libro not in self.libros:
            self.libros.append(libro)


class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.libros = []

    def agregarLibro(self,libro):
        if libro not in self.libros:
            self.libros.append(libro)

    def eliminarLibro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

    def mostrarListaLibros(self):
        for libro in self.libros:
            print(libro.mostrarLibro())


def main():

    libro1 = Libro("978-0-14-118253-7", "Lolita", 1955)
    libro1.agregarAutor("Vladimir Nabokov")
        
    autor1 = Autor("Vladimir Nabokov","Ruso-Estadounidense")

    biblioteca1 = Biblioteca("Torrente Ballester","Garrido, Salamanca")

    biblioteca1.agregarLibro(libro1)
    
    biblioteca1.mostrarListaLibros()
    

    

