
#! Decorators
# Decorators are a powerful feature that allows you to modify or extend the behavior of functions or methods without changing their actual code. Decorators are implemented using functions themselves, and they typically take a function as an argument, modify it in some way, and then return the modified function or a new function altogether.

#! Creating a decorator
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



