# we separate functionality in modules
# these modules will be imported
# SYNTAX
# import module / module.function(params) / import module as my_name / from <module> import <element>

import math
result = math.pow(9,2)
print(result)
print(math.pi)

import math as math_functions
print(math_functions.cos(85))

from math import pi as pi_number
print(pi_number)