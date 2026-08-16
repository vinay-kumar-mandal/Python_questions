# Take a month number and print the number of days in that month, handling February separately.
month_number = int(input("Enter month number (1-12): "))


def print_days_in_month(month_number):
    if month_number < 1 or month_number > 12:
        print("Invalid month number! Please enter a number between 1 and 12.")
        return

    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month_number in [4, 6, 9, 11]:
        days = 30
    elif month_number == 2:
        days = "28 or 29 (leap year)"
    
    print(f"Month {month_number} has {days} days.")

if __name__ == "__main__":
    print_days_in_month(month_number)
