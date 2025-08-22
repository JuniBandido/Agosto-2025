dispDicc = {}

class Dispositivos:
    def __init__(self, iD, marca, modelo, direccion_ip):
        super().__init__()
        self.marca = marca
        self.modelo = modelo
        self.direccion_ip = direccion_ip
        self.iD = iD

    def showInfo(self):
        return f"ID: {self.iD}\nMarca: {self.marca}\nModelo: {self.modelo}\nDireccion IP: {self.direccion_ip}"

class Computadora(Dispositivos):
    def __init__(self, iD, marca, modelo, direccion_ip, usuario_asignado, sistema_operativo):
        super().__init__(iD, marca, modelo, direccion_ip)
        self.usuario_asignado = usuario_asignado
        self.sistema_operativo = sistema_operativo

class Impresora(Dispositivos):
    def __init__(self, iD, marca, modelo, direccion_ip, tipo_impresion):
        super().__init__(iD, marca, modelo, direccion_ip)
        self.tipo_impresion = tipo_impresion

class RegistrarComputadora(Computadora):
    def add(self):
        dispDicc[x.iD] = {
            "marca": x.marca,
            "modelo": x.modelo,
            "direccion_ip": x.direccion_ip,
            "ususario": x.usuario_asignado,
            "sistem_op": x.sistema_operativo
        }

    def show(self):
        print(f"{x.showInfo()}\nUsuario Asignado: {x.usuario_asignado}\nSistema Operativo: {x.sistema_operativo}")

    def delete(self):
        if not dispDicc:
            print("No hay nada en el diccionario!")
        else:
            toRemove = input("Ingrese el ID del dispositivo que quiere eliminar: ")
            for i in dispDicc:
                if i.lower() == toRemove.lower():
                    dispDicc.pop(i)

class RegistrarImpresora(Impresora):
    def add(self):
        dispDicc[x.iD] = {
            "marca": x.marca,
            "modelo": x.modelo,
            "direccion_ip": x.direccion_ip,
            "tipo_impresion": x.tipo_impresion
        }
while True:
    menu = input("1. Agregar Computadora\n2. Agregar Impresora\n3. Mostrar Lista de dispositivos\n4. Eliminar por ID\n5. Salir\nSeleccione una opcion (1-5): ")
    match menu:
        case "1":
            x = Computadora(input("Ingrese su ID: "), input("Ingrese la marca: "), input("Ingrese modelo: "), input("Ingrese su direccion ip: "), input("Ingrese el usuario: "), input("Ingrese el sistema operativo: "))
            RegistrarComputadora.add(x)

        case "2":
            x = Impresora(input("Ingrese su ID: "), input("Ingrese la marca: "), input("Ingrese modelo: "), input("Ingrese su direccion ip: "), input("Ingrese el tipo de impresion: "))
            RegistrarImpresora.add(x)

        case "3":
            for i in dispDicc:
                print(

                )


