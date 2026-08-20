# Find the sum of numbers from 1 to n without using the formula n(n+1)/2.

n = int(input("The sum of numbers from 1 to n."))

def sum_built_in(n):
    return sum(range(1, n+1))

print(sum_built_in(n))