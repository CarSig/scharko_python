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



