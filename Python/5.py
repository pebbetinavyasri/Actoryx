def arithmetic_operations(num1, num2):
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
        print("Modular:", num1 % num2)
    else:
        print("Division and Modular by zero is not allowed")

# User inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function call
arithmetic_operations(num1, num2)