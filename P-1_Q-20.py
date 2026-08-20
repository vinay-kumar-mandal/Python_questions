# Find the sum of all even numbers from 1 to n.
n = int(input("Enter the value of n:"))

k = n // 2

even_sum = k * (k + 1)

print(f"The sum of even numbers from 1 to {n} is: {even_sum}")