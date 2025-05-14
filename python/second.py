import sys

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply
}

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <operation> <num1> <num2>")
        print("Operations: add, subtract, multiply")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = int(sys.argv[2])
        num2 = int(sys.argv[3])
    except ValueError:
        print("Error: num1 and num2 must be integers.")
        sys.exit(1)

    if operation in operations:
        result = operations[operation](num1, num2)
        print(result)
    else:
        print("Invalid operation. Please use add, subtract, or multiply.")
        sys.exit(1)


if __name__ == "__main__":
    main()