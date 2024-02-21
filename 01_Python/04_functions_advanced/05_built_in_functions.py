# print(): Used to display output to the console.
print("Hello, world!")

# input(): Reads input from the user via the console.
name = input("Enter your name: ")


# len(): Returns the length of an object such as a string, list, or tuple.
length = len("Python")

# type(): Returns the type of an object.
x = 5
print(type(x))  # <class 'int'>

# int(), float(), str(): Convert values to integers, floats, or strings, respectively.
num = int("10")

# range(): Generates a sequence of numbers.


for i in range(5):
    print(i)

# max(), min(), sum(): Returns the maximum, minimum, or sum of values in an iterable.
numbers = [5, 10, 3]
max_value = max(numbers)
min_value = min(numbers)
sum_value = sum(numbers)


# sorted(): Returns a sorted list from the elements of an iterable.
sorted_list = sorted([3, 1, 2])

# abs(), round(): Returns the absolute value (distance from 0) or rounds a floating-point number to a specified number of decimal places.


absolute_value = abs(-5)