#Example of a function that calculates the factorial of a number using recursion:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)