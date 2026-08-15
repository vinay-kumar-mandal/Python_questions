#  Take a year and determine whether it is a leap year.
num = int(input("Enter a number:"))

if num % 4 == 0:
    print(f"{num} is a leap year.")
else:
    print(f"{num} is not a leap year.")