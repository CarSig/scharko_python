
# Variable-length arguments
def greetMulti(*names):
    return f"Hello, {', '.join(names)}"

print(greetMulti("John", "Jane", "Alice"))  # Output: Hello, John, Jane, Alice

# Lambda functions
lambdaGreet = lambda name, name2: f"Hello, {name} and {name2}"

print(lambdaGreet("John","Jane"))  # Output: Hello, John and Jane

# Function can be passed as an argument to another function

def add(a, b):
    return a + b

print (add(3, add(1,1)))  # Output: 5

# And even into itself (recursion)
def factorial(n):
    if n == 0:
        print("n is 0")
        return 1
    else:
        print(f"n is {n}")
        return n * factorial(n - 1)
    
print(factorial(7))     



