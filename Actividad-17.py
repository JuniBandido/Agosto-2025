class Estudiante:
    def __init__(self, name, carnet, grade):
        self.name = name
        self.carnet = carnet
        self.grade = grade

students = []

while True:
    menu = input(
        "1. Agregar estudiante\n2. Eliminar estudiante\n3. Buscar estudiante\n4. Ordenar lista al revés\n5. Salir\nEscoja una opcion (1-5): ")
    print()
    match menu:
        case "1":
            studentName = input("Ingrese el nombre del estudiante: ")
            studentCarnet = input(f"Ingrese el carnet de {studentName}: ")
            studentGrade = input(f"Ingrese el grado {studentName}: ")
            print()
            currentStudent = Estudiante(studentName, studentCarnet, studentGrade)
            students.append(currentStudent)

        case "2":
            if not students:
                print("No hay estudiantes registrados")
                print()
            else:
                count = 0
                studentCarnet = input("Ingrese el carnet del estudiante que quiere eliminar: ")
                for i in students:
                    count += 1
                    if studentCarnet == students[count].carnet:
                        students.remove(students[count])

        case "3":
            if not students:
                print("No hay estudiantes registrados!")
                print()
            else:
                count = 0
                studentSearch = input("Ingrese el nombre de del estudiante que quiere buscar: ")
                for i in students:
                    if studentSearch == students[count].name:
                        print(f"Nombre: {students[count].name}\nCarnet: {students[count].carnet}\nGrado: {students[count].grade}")
                        print()
                        count += 1

        case "4":
            print("Se pondrán los ultimos registrados al principio de la lista")
            students.reverse()

        case "5":
            print("Hasta pronto!")
            break

        case _:
            print("Opcion no disponible")