#Herencia simple y jerarquica

class SerVivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print("El ser vivo respira")

class Humano(SerVivo):
    def hablar(self):
        print("El humano habla")

class Animal(SerVivo):
    def caminar(self):
        print("El animal camina")

#Herencia multiple

class Persona():
    def estarVivo(self):
        print("Una persona está viva")

class Estudiante():
    def irAClase(self):
        print("El estudiante va a clase")

class NuevoEstudainte(Persona, Estudiante):
    def nuevo(self):
        print("El nuevo estudiante va a clase")

x = NuevoEstudainte()

x.nuevo()
x.irAClase()

#Herencia multinivel

class Ninio(SerVivo):
    def ninio(self):
        print("El niño es un ser vivo")

class Bebe(Ninio):
    def bebe(self):
        print("El bebe llora")



