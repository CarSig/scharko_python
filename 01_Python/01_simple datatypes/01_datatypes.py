
    
# Classes and objects
# Creating a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, {self.name}"
# Creating an object
person = Person("John", 25)
# Accessing attributes
name = person.name
# Calling methods
greeting = person.greet()

# Modules
# Importing a module
import math
# Using functions from a module
value = math.sqrt(25)
# Importing specific functions
from math import sqrt
# Using specific functions
value = sqrt(25)
# Renaming a module
import math as m
# Using a renamed module
value = m.sqrt(25)
# Creating a module
# mymodule.py
def greet(name):
    return f"Hello, {name}"
# Using a module
# import mymodule
# greeting = mymodule.greet("John")

# File handling
# Opening a file
file = open("example.txt", "r")
# Reading a file
content = file.read()
# Writing to a file
file = open("example.txt", "w")
file.write("Hello, World!")
# Closing a file
file.close()

# Exception handling
# try and except
try:
    value = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
# finally
try:
    value = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")

# Regular expressions
import re
# search()
pattern = "hello"
string = "hello, world"
result = re.search(pattern, string)
# match()
pattern = "hello"
string = "hello, world"
result = re.match(pattern, string)

# List comprehensions
# Creating a list
example_list = [1, 2, 3, 4, 5]
# Using list comprehensions
squared_list = [x ** 2 for x in example_list]

# Generators
# Creating a generator
def example_generator():
    yield 1
    yield 2
    yield 3
# Using a generator
generator = example_generator()
value = next(generator)

# Decorators
# Creating a decorator
def example_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
# Using a decorator
@example_decorator
def greet():
    print("Hello, World!")
greet()

# Virtual environment
# Creating a virtual environment
# python -m venv myenv
# Activating a virtual environment
# Windows
# myenv\Scripts\activate
# macOS and Linux
# source myenv/bin/activate
# Deactivating a virtual environment
# deactivate

# Debugging
# Using print statements
print("Hello, World!")
# Using the debugger
# import pdb
# pdb.set_trace()
# Using the traceback module
import traceback
try:
    value = 10 / 0
except ZeroDivisionError:
    traceback.print_exc()

# Testing
# Using the unittest module
import unittest
class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(10 + 5, 15)
# Running tests
# python -m unittest test_example.py
        
# Version control
# Initializing a repository
# git init
        


