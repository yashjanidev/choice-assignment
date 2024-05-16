number = int(input("Enter a number: "))

def factorial(number):
    if number == 0:
        return 1
    if number < 0:
        return "Please enter Positive number"
    else:
        return number * factorial(number-1)

result = factorial(number)
print(f"Factorial is: {result}")
