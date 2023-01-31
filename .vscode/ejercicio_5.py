""" Notas de clase: Dado el siguiente diccionario, escriba un programa que
imprima en pantalla el promedio de notas del estudiante. Debe imprimirlo en
un diccionario de la forma {"nombre": 75}
sampleDict = {
"class": {
"student": {
"name": "Mike",
"marks": {
"physics": 70,
"history": 80,
"math: 90
},
}
}
} """


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# solution
print(sampleDict['class'])
print("Promedio: ", (sampleDict['class']['student']['marks']['history']))
