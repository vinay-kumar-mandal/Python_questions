# Take a number and determine whether it is positive, negative, or zero.
num = float(input("Enter a number:"))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")

    continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
