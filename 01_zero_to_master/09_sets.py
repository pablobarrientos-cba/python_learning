# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference,
# and symmetric difference.

# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {};
# the latter creates an empty dictionary

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket2 = {'apple', 'orange'}
print(basket)

print('apple' in basket)
print('pine apple' in basket)

# Methods include set operation like union, intersection, subset, superset and so on
print(basket2.issubset(basket))
print(basket2.issuperset(basket2))
print(basket.intersection(basket2))
