# string

# multiline

from re import X

multi = """
This is a multi line in the python world
I have never seen anything
like this before
"""

x = False
if x:
    print("Es verdad")
elif not X:
    print("oops")
else:
    print("Es mentira")

# lists are mutable
numbers = [1, 2, 3, 4]
numbers.sort(reverse=True)

# tuples are immutable 
numbers_tuple = (0, 1, 2, 3)
numbers_tuple.count(4)

# dictionaries (key, value pairs)
my_dict = {'Gino': 21, 'Feli': 7, 'Paul': 14}

del my_dict["Gino"]

print(multi)
