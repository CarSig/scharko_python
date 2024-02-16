# here are all comprehensions in Python:
# Comprehensions are a feature in Python that allows you to create sequences from other sequences. They provide a more concise and readable way to create sequences. There are four types of comprehensions in Python:
#
# List comprehensions
# Dictionary comprehensions
# Set comprehensions
# Generator (tuple) comprehensions
#


# List comprehensions
# [expression for item in iterable]

# Example
# # Using a loop
example_list = [1, 2, 3, 4, 5]
squared_list = []
for x in example_list:
    squared_list.append(x ** 2)
# # Using list comprehensions
squared_list = [x ** 2 for x in example_list]


# Dictionary comprehensions
# {key: value for item in iterable}

# Example
# # Using a loop
example_list = [1, 2, 3, 4, 5]
squared_dict = {}
for x in example_list:
    squared_dict[x] = x ** 2
# # Using dictionary comprehensions
squared_dict = {x: x ** 2 for x in example_list}


# Set comprehensions
# {expression for item in iterable}

# Example
# # Using a loop
example_list = [1, 2, 3, 4, 5]
squared_set = set()
for x in example_list:
    squared_set.add(x ** 2)
# # Using set comprehensions
squared_set = {x ** 2 for x in example_list}


# Generator comprehensions
# (expression for item in iterable)

# Example
# # Using a loop
example_list = [1, 2, 3, 4, 5]
squared_generator = (x ** 2 for x in example_list)
# # Using generator comprehensions
squared_generator = (x ** 2 for x in example_list)
# # Using a generator
generator = squared_generator

