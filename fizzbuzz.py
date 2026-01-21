# FizzBuzz: 1 a 50
# Múltiplo de 3 → "Fizz", de 5 → "Buzz", de ambos → "FizzBuzz", si no → el número

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
