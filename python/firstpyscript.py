import sys
import os

operation = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

def add(num1, num2):
    return add
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2

if operation == "add":
    result = add (num1 , num2)
    print(result)
elif operation == "subtract":
    result = subtract (num1 , num2)
    print(result)
elif operation == "multiply":
    result = multiply (num1 , num2)
    print(result)
else:
    print("Invalid operation. Please use add, subtract, or multiply.")
    sys.exit(1)
