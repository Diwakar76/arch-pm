def add_numbers(a, b):
    return a + b

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print("Result:", result)
except Exception as e:
    print("Error:", e)

# This code defines a function to add two numbers and handles user input.
# It includes error handling to manage invalid inputs gracefully.


# The function add_numbers takes two arguments and returns their sum.
# The try-except block captures any exceptions that may occur during input or calculation.