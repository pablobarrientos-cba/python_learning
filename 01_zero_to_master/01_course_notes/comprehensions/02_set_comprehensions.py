# Set comprehensions make reference to a feature in Python
# that allows us to create list in one line avoiding looping
# Structure -> param/expression for param in iterable (if condition)
# The same as list comprehensions, we only need to change the [] by {}

list1 = {char.upper() for char in 'hello'}
print(list1)

list2 = {num for num in range(1, 51)}
print(list2)

list3 = {num ** 2 for num in range(1, 51)}
print(list3)

list4 = {num ** 2 for num in range(1, 51) if num % 2 == 0}
print(list4)
