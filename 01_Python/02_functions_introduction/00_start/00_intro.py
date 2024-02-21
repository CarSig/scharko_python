
#? Functions in Python are blocks of organized, reusable code that perform a specific task. They allow you to break down your program into smaller pieces

#! Defining a Function:
# To define a function in Python, you use the def keyword followed by the function name and parentheses (), which may include parameters. The function block starts with a colon : and is indented.
def greet():
    print("Hello, world!")

#! Calling a Function:
# To execute or use a function, you call it by its name followed by parentheses ().
greet()  # Calling the greet function


#! Parameters and Arguments:
# Functions can accept input parameters (arguments) which are values passed to the function when it is called. These parameters are specified within the parentheses in the function definition.

def greetInput(name):
    print("Hello, " + name + "!")

greetInput("Scharko")  # Passing the argument "Scharko" to the greet function


# Return Statement:
# Functions can  return a value using the return statement. This value can then be used elsewhere in your code. This is most common use of functions

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8







