# Take a temperature in Celsius and classify it as freezing, cold, normal, hot, or very hot using reasonable ranges.
temp = float(input("Enter temperature in Celsius: "))
if temp <= 0:
    print(f"{temp}°C is freezing.")
elif 0 < temp <= 10:
    print(f"{temp}°C is cold.")
elif 10 < temp <= 25:
    print(f"{temp}°C is normal.")
elif 25 < temp <= 35:
    print(f"{temp}°C is hot.")
else:
    print(f"{temp}°C is very hot.")
    