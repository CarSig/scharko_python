
# Importing modules in Python follows some rules and best practices to ensure clarity, readability, and maintainability of your code. Here are some rules and guidelines for importing modules in Python:

# Explicit is better than implicit:
# Always import modules explicitly rather than using wildcard imports (from module import *). This helps in understanding where each function or class comes from.

# # Avoid
# from module import *
# Import each module on a separate line:
# Import each module on a separate line to make your imports clear and easy to read.

# python
# Copy code
# # Good
# import module1
# import module2

# # Avoid
# import module1, module2
# Import statements order:
# Follow a specific order for importing modules:

# Standard library imports
# Related third-party imports
# Local application/library-specific imports
# python
# Copy code
# # Good
# import os
# import sys
# import pandas as pd

# # Avoid
# import pandas as pd
# import os, sys
# Avoid circular imports:
# Circular imports occur when two modules depend on each other. Avoid this situation as it can lead to unexpected behavior. Refactor your code to remove circular dependencies.

# Use import aliases sparingly:
# While aliasing imports (import module as alias) can sometimes improve readability, overuse can make your code less clear. Use aliases sparingly and only when it improves readability.

# python
# Copy code
# # Good
# import pandas as pd
# import numpy as np

# # Avoid
# import pandas as p
# import numpy as n
# Avoid importing unnecessary modules:
# Import only the modules you need for your current code. Importing unnecessary modules can increase the size of your codebase and potentially introduce conflicts or bugs.

# Consider importing specific names:
# Instead of importing entire modules, consider importing only the specific names (functions, classes, or variables) you need from those modules. This can improve performance and reduce namespace clutter.

# python
# Copy code
# # Good
# from module import function

# # Avoid
# import module
# Following these rules and best practices will help keep your Python code organized, maintainable, and easy to understand.




# Modules
# Importing a module
import math
# Using functions from a module
value = math.sqrt(25)
# Importing specific functions
from math import sqrt
# Using specific functions
value = sqrt(25)
# Renaming a module
import math as m
# Using a renamed module
value = m.sqrt(25)
# Creating a module
# mymodule.py
def greet(name):
    return f"Hello, {name}"
# Using a module
import mymodule
greeting = mymodule.greet("John")




