#lambdas

sum_values = lambda first_value, second_value: first_value + second_value

print(sum_values(3,6))

multiply_values = lambda first_value, second_value: first_value * second_value
print(multiply_values(3,6))

def sum_values_three(value):
    return lambda first_value, second_value: first_value * second_value + value

print(sum_values_three(5)(3,6))