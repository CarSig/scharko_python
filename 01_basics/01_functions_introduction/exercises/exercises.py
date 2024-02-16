# MATH FUNCTIONS



# function sum
def sum(a, b):
    return a + b

# function subtract
def subtract(a, b):
    return a - b

# function multiply
def multiply(a, b):
    return a * b

# function divide
def divide(a, b):
    return a / b

# function power
def power(a, b):
    return a ** b

# function square
def square(a):
    return a ** 2

# function cube
def cube(a):
    return a ** 3


# STRING MANIPULATION FUNCTIONS

# function reverse
def reverse(text):
    return text[::-1]

# function capitalize
def capitalize(text):
    return text.capitalize()

# function uppercase
def uppercase(text):
    return text.upper()

# function lowercase
def lowercase(text):
    return text.lower()



# function length
def length(text):
    return len(text)

# function is_palindrome
def is_palindrome(text):
    return text == reverse(text)


print(is_palindrome("radar"))
print(is_palindrome("hello"))

# Implement a function to find and return the index of a specific character in a string.

# function find
def find(text, char):
    return text.index(char)



# LIST MANIPULATION FUNCTIONS

# function add
def add(lst, item):
    lst.append(item)
    return lst

# function remove
def remove(lst, item):
    lst.remove(item)
    return lst

# function reverse
def reverseList(lst):
    return lst[::-1]

# fizzbuzz

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Write a function that checks if a number is even or odd.
            
def is_even(n):
    return n % 2 == 0
            
# Create a function that returns the maximum of three numbers.

def maximum(a, b, c):
    return max(a, b, c)


# Implement a function that checks if a given year is a leap year.
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# Define a function to check if a number is prime.
