# Funciones de orden superior
from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sumas_function(val_one, val_two, _function):
    return _function(val_one + val_two)


print(sumas_function(1, 2, sum_five))
print(sumas_function(1, 2, sum_one))

# Closures


def sum_ten(valor):
    def add(value):
        return value + 10 + valor
    return add


closure_var = sum_ten(20)
print(closure_var(20))
print(sum_ten(20)(10))

# Built-in con funciones de orden superior

numbers = [2, 5, 10, 21, 3, 30, 40]

# map
def double(val):
    return val * 2


print(list(map(double, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# filter
def filter_greater_than_ten(val):
    return val > 10

mayores = list(filter(filter_greater_than_ten, numbers))
mayores_with_lambda = list(filter(lambda num: num > 10, numbers)) 
print(mayores)
print(mayores_with_lambda)

# reduce
def sum_two_values(first_val, second_val):
    return first_val + second_val

suma = reduce(sum_two_values, numbers)
print(suma)
print(reduce(lambda val1, val2: val1 + val2, numbers))