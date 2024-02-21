# Dictionaries

# Dictionary is a collection of key-value pairs. It is a mutable, unordered, and indexed collection. Dictionaries are created using curly braces. Each key-value pair is separated by a colon. Keys are unique and immutable. Values can be of any data type.

# Creating a dictionary
example_dictionary = {"name": "John", "age": 25}
# Accessing elements
name = example_dictionary["name"]
# Modifying elements
example_dictionary["name"] = "Jane"
# Adding elements
example_dictionary["company"] = "Scharko"
# Removing elements
example_dictionary.pop("name")
# Looping through a dictionary
for key, value in example_dictionary.items():
    print(f"{key}: {value}")

print (example_dictionary)    