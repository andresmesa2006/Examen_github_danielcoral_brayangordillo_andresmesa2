import csv

def crear_curso():
    curso = input("Ingrese código de curso: ")
    nombre = input("Ingrese nombre del curso: ")
    instructor = input("Ingrese nombre del instructor: ")
    description = input("Ingrese la descripción del curso: ")

    with open('data/courses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([curso, nombre, instructor, description])
    
    print("Curso creado exitosamente")
    return curso

def agregar_estudiante(curso):
    codigo_de_estudiante = input("Ingrese TI de estudiante: ")

    with open('data/students.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([codigo_de_estudiante, curso])
    
    print("Estudiante agregado exitosamente")

