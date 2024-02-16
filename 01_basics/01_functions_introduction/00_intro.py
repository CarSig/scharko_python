# Functions in Python are blocks of organized, reusable code that perform a specific task. They allow you to break down your program into smaller, modular pieces, making your code easier to understand, debug, and maintain. 
# Defining a Function:
# To define a function in Python, you use the def keyword followed by the function name and parentheses (), which may include parameters. The function block starts with a colon : and is indented.


def greet():
    print("Hello, world!")

# Calling a Function:
# To execute or use a function, you call it by its name followed by parentheses ().


greet()  # Calling the greet function


# Parameters and Arguments:
# Functions can accept input parameters (arguments) which are values passed to the function when it is called. These parameters are specified within the parentheses in the function definition.

python
Copy code
def greet(name):
    print("Hello, " + name + "!")

greet("Scharko")  # Passing the argument "Alice" to the greet function

# Return Statement:
# Functions can optionally return a value using the return statement. This value can then be used elsewhere in your code.


def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# Documentation (Docstrings):
# It's good practice to include documentation (docstrings) within your function to describe what it does. This helps other programmers (and your future self) understand how to use the function.


def greet(name):
    """
    This function greets the user.
    """
    print("Hello, " + name + "!")


# Scope of Variables:
# Variables defined inside a function are scoped only within that function (local scope), while variables defined outside a function are accessible globally.

# Default Arguments:
# You can specify default values for function parameters, which are used when the function is called without providing a specific argument for that parameter.


def greet(name="Scharko"):
    print("Hello, " + name + "!")

greet()          # Output: Hello, world!
greet("Alice")   # Output: Hello, Alice!