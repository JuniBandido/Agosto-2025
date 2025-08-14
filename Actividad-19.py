listCoockies = []

class Galletas:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def mostrar_info(self):
       print(f"Nombre Galleta: {self.name} | Precio: {self.price} | Peso: {self.weight}")

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

class RegistrarBasica(Galletas):
    def registrar_galleta_basica(self):
        name = input("Ingresa el nombre: ")
        price = int(input("Ingresa el precio: "))
        weight = input("Ingresa el peso: ")
        print()
        listCoockies.append(Galletas(name, price, weight))

def mostrar_galletas():
    if not listCoockies:
        print("No hay galletas registradas!")
    else:
        print("\nLista de galletas:")
        i = 1
        for x in listCoockies:
            print(f"{i}. ", end="")
            x.mostrar_info()
            i += 1
    print()

def buscar_nombre():
    if not listCoockies:
        print("No hay galletas registradas!")
    else:
        x = input("Ingrese el nombre de la galleta que quiere buscar: ").lower()
        for i in listCoockies:
            if x == i.name.lower():
                i.mostrar_info()
    print()

def eliminar_nombre():
    if not listCoockies:
        print("No hay galletas registradas!")
    else:
        x = input("Ingrese el nombre de la galleta que quiere eliminar: ")
        for i in listCoockies:
            if x.lower() == i.name.lower():
                listCoockies.remove(i)
    print()

while True:
    menu = input("1. Agregar galleta\n4. Mostrar Lista\n5. Buscar por nombre\n6. Eliminar\n7. Salir\nEscoja una opcion: ")
    print()
    match menu:
        case "1":
            RegistrarBasica.registrar_galleta_basica(Galletas)

        case "4":
            mostrar_galletas()

        case "5":
            buscar_nombre()

        case "6":
            eliminar_nombre()

        case "7":
            print("Hasta pronto!")
            break

        case _:
            print("Opcion no valida")