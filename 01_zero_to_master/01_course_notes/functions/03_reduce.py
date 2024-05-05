from functools import reduce

my_list = [1, 2, 3]
letters = ['h', 'e', 'l', 'l', 'o']


def accumulate(value, item):
    return value + item


def concat(value, item):
    return value + ' ' + item


# reduce function performs an action and returns a single value
result = reduce(accumulate, my_list, 0)
print(result)

result = reduce(concat, letters)
print(result)
