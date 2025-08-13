listCoockies = []

class Galletas:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def mostrar_info(self):
       return f"Nombre Galleta: {self.name}\nPrecio: {self.price}\nPeso: {self.weight}"

class GalletaChispas(Galletas):
    def cantidad_chispas(self):
        while True:
            try:
                x = int(input("Ingrese la cantidad de chispas: "))
                if x < 0:
                    raise ValueError
            except ValueError:
                print("Valor no válido")
            else:
                return f"{Galletas.mostrar_info(self)}, y tiene {x} chispas"

class Relleno:
    def sabor_relleno(self):
        y = input("Agregue el sabor del relleno: ")
        return f"El sabor del relleno es de {y}"

    def describir_relleno(self):
        z = input("Describa el relleno: ")
        return f"el relleno es {z}"

class GalletaRellena(Galletas, Relleno):
    def mostrar_galletaRellena(self):
        return f"{Galletas.mostrar_info(self)}, {Relleno.sabor_relleno(self)} y {Relleno.describir_relleno(self)}"

class RegistrarGalletaBasica:
    def add(self):
        try:
            name = input("Ingrese el nombre de la galleta: ")
            price = int(input("Ingrese el precio de la galleta: "))
            weight = input("Ingrese el peso de la galleta: ")
            listCoockies.append(Galletas(name, price, weight))
            print("Galleta agregada!")
        except ValueError:
            print("El precio debe ser un número")

    def delete(self):
        coockieToDelete = input("Ingrese el nombre de la galleta que quiere eliminar: ")
        for i in listCoockies:
            if i.name.lower() == coockieToDelete.lower():
                listCoockies.remove(i)
                print("Galleta eliminada")

    def show(self):
        if not listCoockies:
            print("No hay galletas registradas")
        else:
            for i, x in enumerate(listCoockies, start=1):
                print(f"{i}. {x.mostrar_info()}")

i = RegistrarGalletaBasica()
i.add()
i.show()
i.delete()
print(listCoockies)