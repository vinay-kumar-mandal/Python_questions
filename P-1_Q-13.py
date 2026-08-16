def calculator():
    print("--simple calculator----")

    try:
        num1 = float(input("Enter first number:"))
        op = input("Enter operator(+, -, *, /, %):")
        num2 = float(input("Enter second number:"))

        if op == '+': 
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        elif op == '%':
            result = num1 % num2 if num2 != 0 else "Error! Division by zero."
        else:
            result = "Invalid operator!"
    except ValueError:
        result = "Invalid input! Please enter numeric values."
    print(f"Result: {result}")
   
if __name__ == "__main__":
    calculator()