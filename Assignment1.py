# Using regular function
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    return n * factorial(n-1)

# Using lambda with reduce function
from functools import reduce
factorial_lambda = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))

# Test both methods
number = 5

print(f"Factorial of {number} using regular function:", factorial(number))
print(f"Factorial of {number} using lambda function:", factorial_lambda(number))