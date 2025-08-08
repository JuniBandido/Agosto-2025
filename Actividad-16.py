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
    print()

    match menu:
        case "1":
            titulo_libro = input("Ingrese el titulo del libro: ")
            autor_libro = input("Ingrese el autor del libro: ")
            publicacion_libro = input("Ingrese el año de publicación: ")
            print()

            book1 = Libro(titulo_libro, autor_libro, publicacion_libro)

            books.append(book1)

        case "2":
            if not books:
                print("No hay libros registrados")
                print()
            else:
                count = 0
                for i in books:
                    print(f"Titulo: {books[count].tittle}")
                    print(f"Autor: {books[count].author}")
                    print(f"Año de publicación: {books[count].publiYear}")
                    print()
                    count += 1

        case "3":
            libro = input("Ingrese el titulo del libro que quiere eliminar: ").lower()
            count = 0
            for i in books:
                if libro == books[count].tittle.lower():
                    books.remove(books[count])
                else:
                    print("Pelicula no encontrada")

        case "4":
            print("Hasta pronto!")
            break

        case _:
            print("opcion invalida")
            print()