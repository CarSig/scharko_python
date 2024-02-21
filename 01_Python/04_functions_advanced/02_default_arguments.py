# Default Arguments:
# You can specify default values for function parameters, which are used when the function is called without providing a specific argument for that parameter.


def greetOptional(name="Scharko"):
    print("Hello, " + name + "!")

greetOptional()          # Output: Hello, world!
greetOptional("Alice")   # Output: Hello, Alice!