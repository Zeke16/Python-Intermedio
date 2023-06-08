# Manejo de ficheros

# .txt

import os

text_file = open("Python Intermedio/my_file.txt", "w+")
#print(text_file.read()) # Leer todo el archivo
#print(text_file.readline()) # Leer una linea
#print(text_file.readlines()) # Leer todas las lineas y guardarlas como array
text_file.write("\nNueva linea") # Agregar una nueva linea
text_file.close()
text_file = open("Python Intermedio/my_file.txt", "r")
print(text_file.read())
text_file.close() # Cerrar la lectura

#os.remove("Python Intermedio/my_file.txt")

# .json 

import json

text_file_json = open("Python Intermedio/my_file.json", "w+")

json_test = {
    "nombre": "zeke",
    "apellido": "ramirez",
    "edad": 23
}
json.dump(json_test, text_file_json, indent=4)

text_file_json.close()

text_file_json = json.load(open("Python Intermedio/my_file.json", "r"))
print(text_file_json)
print(type(text_file_json))

# .csv

import csv

csv_file = open("Python Intermedio/my_file.csv", "w+", newline='')

csv_writter = csv.writer(csv_file)
csv_writter.writerow(["nombre", "apellido", "edad"])
csv_writter.writerow(["Ezequiel", "Ramirez", 23])