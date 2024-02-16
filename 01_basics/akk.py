
# Exception handling
# try and except
try:
    value = 10 / 0
except Exception as e:
    print("Cannot divide by zero",e)
finally:
    print("This will always execute")


try:
    value = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")





