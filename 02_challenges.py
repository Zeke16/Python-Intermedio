## Challenges

#FizzBuzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Value: {i} -> FizzBuzz")
    elif i % 5 == 0:
        print(f"Value: {i} -> Buzz")
    elif i % 3 == 0:
        print(f"Value: {i} -> Fizz")
    else:
        print(f"Value: {i}")

#Anagrama

def anagram(string1, string2):
    if string1.lower() == string2.lower():
        return False
    return sorted(string1.lower()) == sorted(string2.lower())

print(anagram("arroza", "zorra"))

#fibonacci

def fibonacci(num):
    prev = 0
    next = 1
    for i in range(1, 51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci(0)

#numero primo

def numeros_primos():
    for i in range(1, 101):

        if i >= 2:
            
            divisible = False

            for index in range(2, i):
                if i % index == 0:
                    divisible = True
                    break
                
            if not divisible:
                print(i)
 
numeros_primos()

# reverse text

def reverse_text(text):
    text_len = len(text)
    reverse = ""
    for index in range(0, text_len):
        reverse += text[text_len - index - 1]
    return reverse;

reverse_text("Hola")