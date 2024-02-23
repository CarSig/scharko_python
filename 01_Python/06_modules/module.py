from othermodul import color , number as n, my_function
import math



print(color)

def whatColor():
    print(f"The color is {color}")

whatColor()


# Using functions from a module
sqrt = math.sqrt(n)
print(sqrt)

power = int(math.pow(n,2))
print(power)

my_function()




