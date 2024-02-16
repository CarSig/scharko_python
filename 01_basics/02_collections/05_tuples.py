# Tuples
# Tuples are similar to lists, but they are immutable. This means that once a tuple is created, you cannot change its values. Tuples are created using parentheses.

# Creating a tuple
example_tuple = (1, 2, 3, 4, 5)
# Accessing elements
first_element = example_tuple[0]
# Slicing
sliced_tuple = example_tuple[1:3]
# Modifying elements
# This will throw an error
# example_tuple[0] = 10
# Looping through a tuple
for element in example_tuple:
    print(element)