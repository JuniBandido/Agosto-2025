from tkinter.messagebox import showinfo


class Libro:
    def __init__(self, tittle, author, publiYear):
        self.tittle = tittle
        self.author = author
        self.publiYear = publiYear

    def showInfo(self):
        print(f"Titulo: {self.tittle}\nAutor: {self.author}\nAño de publicacion: {self.publiYear}")

books = []

while True:
    print("1. Agregar libro")
    print("2. Mostrar lista de libros")
    print("3. Eliminar libro por título")
    print("4. Salir del programa")
    menu = input("Seleccione una opcion: ")

    match menu:
        case "1":
            titulo_libro = input("Ingrese el titulo del libro: ")
            autor_libro = input("Ingrese el autor del libro: ")
            publicacion_libro = input("Ingrese el año de publicación: ")
            print()

            book1 = Libro(titulo_libro, autor_libro, publicacion_libro)

            books.append(book1)

        case "2":
            count = 0
            for i in books:
                print(f"Titulo: {books[count].tittle}")
                print(f"Autor: {books[count].author}")
                print(f"Año de publicación: {books[count].publiYear}")
                print()
                count += 1