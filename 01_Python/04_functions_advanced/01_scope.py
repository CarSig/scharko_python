# Scope defines the visibility and accessibility of variables within a program.
# Python follows the LEGB rule to determine the order in which it searches for variable names:
# Local (L): Variables defined within a function.
# Enclosing (E): Variables defined in the enclosing function (if any).
# Global (G): Variables defined at the top level of a module or explicitly declared as global within a function.
# Built-in (B): Reserved names provided by Python (e.g., print, len, sum).

#! Global Scope:

# Variables defined at the top level of a module (outside of any function) have global scope.
# They can be accessed from anywhere within the module, including inside functions.

# To modify a global variable from within a function, you need to use the global keyword to declare the variable as global.
# python


global_var = 10

def my_function():
    global global_var
    global_var += 5
    print(global_var)

print(global_var)  # Output: 10
my_function()  # Output: 15
print(global_var)  # Output: 15

# ! Local Scope:

# Variables defined within a function have local scope.
# They can only be accessed from within the function in which they are defined.
# Each function call creates a new local namespace, and variables defined within that function are stored in that namespace.

def my_function():
    local_var = 20
    print(local_var)

my_function()  # Output: 20
# print(local_var)  # This will cause an error because local_var is not defined outside the function.

# !Enclosing Scope:

# Variables defined in an enclosing function can be accessed by nested functions.
# Inner functions have access to variables in the outer function's scope.
# This is known as closure or nested scope.


def outer_function():
    outer_var = 30

    def inner_function():
        print(outer_var)

    inner_function()

outer_function()  # Output: 30

# Understanding scope and namespace in Python helps prevent naming conflicts, improves code organization, and ensures that variables are accessed and modified correctly throughout the program.