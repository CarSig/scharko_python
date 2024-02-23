# , for, while, break, continue, pass

# for loop

# 
# Use a for loop when you know the number of iterations in advance or when you need to iterate over a sequence (such as a list, tuple, string, or range).
# The for loop iterates over each item in the sequence, executing the loop body once for each item.

# for item in iterable:
#     expression


# Example
# Loop through a list
print("Loop through a list")
example_list = [1, 2, 3, 4, 5]
for x in example_list:
    print(x ** 2)


# Loop through a string
print("Loop through a string")
example_string = "Hello"
for char in example_string:
    print(char)


# Loop through a dictionary
print("Loop through a dictionary")
example_dict = {"one": 1, "two": 2, "three": 3}
for key, value in example_dict.items():
    print(f"Key: {key}, Value: {value}")

# Loop through a range
print("Loop through a range")
for x in range(5):
    print(x)

# Loop through a range with a step
print("Loop through a range with a step")    
for x in range(0, 10, 2):
    print(x)

# Loop through a range in reverse
print("Loop through a range in reverse")    
for x in range(5, 0, -1):
    print(x)


# while loop
# while condition:
#     expression
    
# Example
# Using a while loop
x = 0
print("Using a while loop")
while x < 5:
    print(x)
    x += 1


#! The continue statement is used within loops (such as for or while loops) to skip the rest of the current iteration and move to the next iteration.
    
# Using continue
print("Using continue")
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

#* The break statement is used to terminate the nearest enclosing loop (such as for or while loop) prematurely.

# Using break
print("Using break")
x = 0
while True:
    print(x)
    x += 1
    if x == 5:
        break

#? The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.        


# Using pass
print("Using pass")
x = 0
while x < 5:
    x += 1
    if x == 3:
        pass
    print(x)



