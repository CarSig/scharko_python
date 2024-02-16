
# Functions
# Creating a function
def greet(name):
    return f"Hello, {name}"
# Calling a function
greeting = greet("John")
# Default arguments
def greet(name="John"):
    return f"Hello, {name}"
# Variable-length arguments
def greet(*names):
    return f"Hello, {', '.join(names)}"
# Lambda functions
greet = lambda name: f"Hello, {name}"
# Recursion
def factorial(n):
    if n == 0:
        print("n is 0")
        return 1
    else:
        print(f"n is {n}")
        return n * factorial(n - 1)
    
print(factorial(7))     