class Atributos:
    def __init__(self, name, password, age):
        self.name = name
        self.__password = password
        self._age = age

y = Atributos("Jose", "123", 10)

class Prueba:
    def __init__(self, name, password, gener):
        self.name = name
        self._gener = gener
        self.__password = password

    @property
    def gener(self):
        return self._gener

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, newpassword):
        if len(newpassword) == 3:
            self.__password = newpassword
        else:
            print("Contraseña no válida")


p = Prueba("juan", "123", "Hombre")

print(p.name, p.gener, p.password)

p.password = "321"

print(p.name, p.gener, p.password)

