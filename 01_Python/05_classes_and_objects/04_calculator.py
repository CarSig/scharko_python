class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Error: Cannot divide by zero.")

    def clear(self):
        self.result = 0

    def get_result(self):
        return self.result


# Example usage
calc = Calculator()
calc.add(5)
calc.subtract(2)
calc.multiply(3)
calc.divide(4)
print(calc.get_result())  # Output: 1.5


# now same using functional programming

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Cannot divide by zero.")
        return None