#modulo para manejar fechas y horas

from datetime import datetime

#Instancia de la fecha actual
now = datetime.now()
print(now)

#creando una fecha con parametros
year_2023 = datetime(2023, 5, 16, 15, 30, 40)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(year_2023)

