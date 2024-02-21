from functools import reduce
# In programming, the term "higher-order" typically refers to functions that can accept other functions as arguments or return functions as results. This concept is central to functional programming paradigms and allows for powerful and flexible code structures. Here's a brief explanation:

#! Accepting Functions as Arguments:
# Higher-order functions can take other functions as arguments. This allows you to pass behavior as an argument to a function, making the code more modular and flexible. For example:


def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result_add = apply_operation(add, 5, 3)  # result_add = 8
result_subtract = apply_operation(subtract, 5, 3)  # result_subtract = 2

#! Returning Functions:
# Higher-order functions can also return functions as results. This allows you to dynamically create functions based on certain conditions or parameters. For example:


def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

result_double = double(5)  # result_double = 10
result_triple = triple(5)  # result_triple = 15

# In this example, the create_multiplier function returns a new function multiplier based on the factor parameter passed to it. This enables the creation of different multiplier functions, such as double and triple, that can then be called with specific arguments.

# Higher-order functions provide a powerful abstraction mechanism, allowing you to write more concise and expressive code by separating concerns and promoting code reuse. They are commonly used in functional programming languages like Python to implement concepts such as map, filter, and reduce, as well as in various design patterns.



# map, filter, and reduce are three commonly used higher-order functions in Python that operate on iterables (such as lists, tuples, or sets) to perform transformations, filtering, and aggregations, respectively.

#! map():

# The map() function applies a given function to each item of an iterable (e.g., a list) and returns an iterator that yields the results.
# It takes two arguments: the function to apply and the iterable to apply it to.
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]


#! filter():

# The filter() function creates an iterator that filters elements of an iterable based on a given function (predicate) and returns only those elements for which the function returns True.
# It takes two arguments: the function to apply as a filter and the iterable to filter.
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4]

# # Filter even numbers using filter and lambda function
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # Output: [2, 4]
# reduce():

# The reduce() function applies a rolling computation to pairs of items in an iterable, from left to right, and returns a single result.
# It's part of the functools module in Python 3 and needs to be imported.


def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # Output: 15