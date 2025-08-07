class Libro:
    def __init__(self, tittle, author, publiYear):
        self.tittle = tittle
        self.author = author
        self.publiYear = publiYear

books = []

print("1. Agregar libro")
print("2. Mostrar lista de libros")
print("3. Eliminar libro por título")
print("4. Salir del programa")
menu = input("Seleccione una opcion: ")

titulo_libro = input("Ingrese el titulo del libro: ")
autor_libro = input("Ingrese el autor del libro: ")
publicacion_libro = input("Ingrese el año de publicación: ")

book1 = Libro(titulo_libro, autor_libro, publicacion_libro)

books.append(book1)

