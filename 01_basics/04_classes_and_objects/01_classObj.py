 
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