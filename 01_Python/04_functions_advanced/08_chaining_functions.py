# chaiining functions

# function chaining is a technique that allows you to call multiple functions in a single line, passing the result of one function to the next. This is a common pattern in functional programming, and it can be useful for creating more readable and expressive code.

# Here's an example of function chaining in Python with string methods:

# #! Function chaining
original_string = "   hello, world   "
result = original_string.upper().replace("WORLD", "universe").strip().capitalize().replace(",", "*****").replace(" ", "#")
print(result)  

# In this example, we start with a string and call the upper method to convert it to uppercase. We then call the replace method to replace the word "world" with "universe". We then call the strip method to remove any leading or trailing whitespace, the capitalize method to capitalize the first letter of the string, and the replace method to replace any commas with asterisks. The result is a single expression that chains together multiple method calls, making it easy to see the sequence of operations being performed.


# with numbers:
a = 5
b = 10

numbers = sum([a, b]).__mul__(2).__add__(10).__sub__(5)
print(numbers) 


