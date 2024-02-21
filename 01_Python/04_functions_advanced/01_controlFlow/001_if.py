# control flow in python
# if, elif, else


# if statement

# The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). The else clause is optional.

# Syntax:
# if condition:
#     # if-block
# else:
#     # else-block


# Example:
# Check if a number is positive or negative
num = 3
if num > 0:
    print("Positive number")
else:
    print("Negative number")

    # elif statement (else if) is used to check multiple conditions
    # Syntax:
    # if condition1:
    #     # if-block1
    # elif condition2:
    #     # elif-block2
    # else:


# example 
temperature = 20
if temperature < 0:
    print("Freezing")
elif temperature < 20:
    print("Cold")
elif temperature < 30:
    print("Normal")
else:
    print("Hot")        