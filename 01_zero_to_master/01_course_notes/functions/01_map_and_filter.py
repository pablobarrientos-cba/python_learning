my_list = [1, 2, 3, 4, 5, 8, 10, 12]


def only_odd(item):
    return item % 2 != 0


def multiply_by(item):
    return item * 2


# map function. When we need to apply certain change on each item in the collection
result = list(map(multiply_by, my_list))
print(result)

# filter function. When we need to evaluate certain condition (bool) on each item/
result = list(filter(only_odd, my_list))
print(result)
