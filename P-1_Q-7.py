# Take marks in five subjects and calculate the percentage and grade.
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
maths = float(input("Enter marks in Maths: "))
hindi = float(input("Enter marks in Hindi: "))
english = float(input("Enter marks in English: "))

total_marks = physics + chemistry + maths + hindi + english
percentage = (total_marks / 500) * 100

print(f"Percentage: {percentage}")