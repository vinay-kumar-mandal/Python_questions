# Find the sum of all odd numbers from 1 to n.


def sum_odd_numbers(n):
    return sum(range(1, n + 1, 2))

n = 10
print(f"Sum of odd numbers from 1 to {n}: {sum_odd_numbers(n)}")
