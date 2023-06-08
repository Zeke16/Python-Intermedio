## Python Package Manager

import numpy # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array({1,2,3,4,5})
print(type(numpy_array))

import pandas # pip install pandas

import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
json_data = response.json()
print(json_data)