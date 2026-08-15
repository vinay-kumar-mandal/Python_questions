#  Take two numbers and print the greater number.
num1 = float(input("Enter first number {num1}:"))
num2 = float(input("Enter Second number {num2}:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"Both numbers are equal: {num1} = {num2}")
