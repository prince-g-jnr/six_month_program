# Modularizing Your Code 2
# 3. Python Modules
# Different ways to Import Modules
# 1. Import the whole modules
import math
# Lets put it to use
print(math.sqrt(9))

# 2. Import as an alias
import math as m
# lets put it to use
print(m.sqrt(25))
# This shortens the module name, this is common with libraries like numpy, pandas, etc

# 3. Import specific functions or variables
from math import sqrt, pi
print(sqrt(36))
print(pi)

# 4. Import everything from the module
from math import *
print(sqrt(49))
print(pi)
# This is usually not recommended because it can conflits if two modules have functions with the same name

# 4. Python Packages
# 5. Code Reuseability
# 6. Organizing a Python Project
