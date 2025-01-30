import csv
 
cursos=[
    {
        "codigo":"001",
        "cursos":"python",
        "estudiantes":[
            {"nombre":"pedro",
             "apellido":"perez",
             "nota1":4, "nota2":3.5, "nota3":5},
        ]
    },
    {
        "codigo":"002",
        "cursos":"java",
        "estudiantes":[
            {"nombre":"juan",
             "apellido":"garcia",
             "nota1":5, "nota2":4.5, "nota3":3},
        ]
    }
]
#crear el archivo csv
with open("reporte_cali.csv", mode="w",newline="") as cali:
    escritor=csv.writer(cali)
    
for curso in cursos:
