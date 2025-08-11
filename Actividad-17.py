class Estudiante:
    def __init__(self, name, carnet, grade):
        self.name = name
        self.carnet = carnet
        self.grade = grade

students = []

while True:
    menu = input(
        "1. Agregar estudiante\n2. Eliminar estudiante\n3. Buscar estudiante\n4. Ordenar lista\n5. Salir\nEscoja una opcion (1-5): ")
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
                    if studentCarnet == students[count]:
                        students.remove(students[count])
                    else:
                        print("No se encontró estudiante")
                print(students[count].name)

