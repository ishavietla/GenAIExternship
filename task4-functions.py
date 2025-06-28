# Recursive factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive Fibonacci function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example
fact_result = factorial(5)
fib_result = fibonacci(6)
print(f"Factorial of 5 is {fact_result}.")
print(f"The 6th Fibonacci number is {fib_result}.")