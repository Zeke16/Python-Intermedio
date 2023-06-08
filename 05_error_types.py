# Tipos de errores

# SyntaxError
# print "Hola comunidad" Error
print("Hola comunidad")  # Correcto

# NameError
# print(name) Error
name = "zeke" # Correcto
print(name) 

# IndexError
lista = [1, 2, 3, 4, 5, 6]
#print(lista[6]) Error
print(lista[5]) # Correcto

# TypeError
# print(lista["Nombres"])
print(lista[0])

# ModuleNotFoundError
# import maths Error
import math

# AttributeError
# print(math.PI) Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Zeke", "Edad": 23}
# print(my_dict["Nombres"]) Error
print(my_dict["Nombre"])

# ImportError
# from math import PII Error
from math import pi

# ValueError
my_int = 10
# my_int = int("10 anios") Error
print(my_int)

# ZeroDivisionError
print(4/4)
# print(4/0) Error