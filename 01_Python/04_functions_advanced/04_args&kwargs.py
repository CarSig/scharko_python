# Variable length arguments (args) and keyword arguments (kwargs) are used to pass a variable number of arguments to a function.

# args are passed as a tuple
# kwargs are passed as a dictionary
def greetArgs(*args):
    return f"Hello, {', '.join(args)}"
def greetKwargs(**kwargs):
    if "age" not in kwargs:
        age = "UNKNOWN AGE"
    else:
        age = kwargs["age"]    
    return f"Hello, {kwargs['person1']} and {kwargs['person2']}. My name is {kwargs['name']} and I am {age} years old."

args = ("John", "Jane")
kwargs = {"person1": "Mark", "person2": "Marry", "name": "Joe"}
print(greetArgs(*args))
print(greetKwargs(**kwargs))

