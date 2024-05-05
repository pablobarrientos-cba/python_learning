from functools import reduce


# 1 Capitalize all the pet names and print the list
def capitalize(item):
    return str(item).capitalize()


my_pets = ['sisi', 'bibi', 'titi', 'carla']
result = list(map(capitalize, my_pets))
print(result)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
result = list(zip(my_strings, sorted(my_numbers)))
print(result)


# 3 Filter the scores that pass over 50%
def over50(item):
    return item > 50


scores = [73, 20, 65, 19, 76, 100, 88]
result = list(filter(over50, scores))
print(result)


# 4 Combine all the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def get_total(value, item):
    return value + item


total = reduce(get_total, (my_numbers + scores))
print(total)
