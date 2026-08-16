#  Calculate a person's final salary after applying different deductions based on salary ranges.
salary = float(input("Enter the person's salary: "))

def calculate_final_salary(salary):
    if salary < 0:
        print("Invalid salary! Please enter a non-negative number.")
        return
    elif salary < 30000:
        deduction = 0.10 * salary  # 10% deduction
    elif salary < 50000:
        deduction = 0.15 * salary # 15% deduction
    elif salary < 100000:
        deduction = 0.20 * salary # 20% deduction
    else:
        deduction = 0.25 * salary # 25% deduction
    final_salary = salary - deduction
    print(f"Final salary after deduction: {final_salary}")
if __name__ == "__main__":
    calculate_final_salary(salary)