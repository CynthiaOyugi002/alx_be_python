print("Welcome to the Python Match-Case Calculator!")
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
        continue
    operation = input("Choose the operation (+, -, *, /) or 'q' to quit: ")

    if operation.lower() == 'q':
        print("Exiting calculator. Goodbye!")
        break
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.\n")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.\n")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.\n")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.\n")
            else:
                result = num1 / num2
                print(f"The result is {result}.\n")
        case _:
            print("Invalid operation. Please choose +, -, *, /, or 'q' to quit.\n")
