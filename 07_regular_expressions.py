## Expresiones regulares

import re as expresion

my_string = "Esta es la leccion #7: Expresiones regulares"
my_other_string = "Esta no es la leccion #7: Expresiones regulares"

# match
match = expresion.match("Esta es la leccion", my_string, expresion.I) # match almacena el rango donde encuentra la coincidencia
start, end = match.span()
print(my_string[start:end])

match = expresion.match("Esta es la leccion", my_other_string) # En caso de no encontrar retorna None
print(match)

# search

search = expresion.search("leccion", my_string) # search busca en todo el string la primer coincidencia
start, end = search.span()
print(my_string[start:end])

# findAll

find_all = expresion.findall("a", my_string) # Encuentra todas las coincidencias
print(find_all)

# split

split = expresion.split(":", my_string) # separa en elementos a partir de una coincidencia de valor
print(split) #almacenados como una lista

# sub

sub = expresion.sub("Expresiones", "expresiones", my_string)
print(sub)

# patters

patters = r"\d" # encontrar todos los numeros
print(expresion.findall(patters, my_string))

patters = r"\D" # encontrar solo letras sin tildes
print(expresion.findall(patters, my_string))