"""""
class Padre:
    def __init__(self, nombre):
        self.nombre = nombre

class Madre:
    def __init__(self, raza):
        self.raza = raza

class Mascotita(Padre, Madre):
    def __init__(self, nombre, raza, nuevo):
        super().__init__(nombre)
        super().__init__(raza)
        self.nuevo = nuevo

x = Mascotita(input("Ingresa el nombre: "), input("Ingresa la raza: "), input("Ingresa el nuevo: "))
print(x.nombre)
print(x.raza)
print(x.nuevo)
"""""
class Padre:
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

class Madre:
    def __init__(self, raza):
        super().__init__()
        self.raza = raza

class Mascotita(Padre, Madre):
    def __init__(self, nombre, raza, nuevo):
        super().__init__(nombre)
        Madre.__init__(self, raza)
        self.nuevo = nuevo

x = Mascotita(input("Ingresa el nombre: "), input("Ingresa la raza: "), input("Ingresa el nuevo: "))
print(x.nombre)
print(x.raza)
print(x.nuevo)
