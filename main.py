import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    continue_calculating = True
    number1 = float(input("What's the first number: "))
    while continue_calculating:
        for op in operations:
            print(op)
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number: "))

        result = operations[operation](number1,number2)
        print(f"{number1} {operation} {number2} = {result}")
        continue_calculating = input("Do you want to continue with the result? (y/n): ") == "y"
        if continue_calculating:
            number1 = result
        else:
            print("\n" * 20)
            calculator()

calculator()