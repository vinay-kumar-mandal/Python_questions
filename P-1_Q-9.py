# Take three angles and determine whether they can form a valid triangle.
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The angles can form a valid triangle.")
else:
    print("The angles cannot form a valid triangle.")
    