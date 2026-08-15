#Take three sides and determine whether they can form a triangle.
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")
    