my_list = [5, 4, 3]

# 1. Get a list with square of the items
print(list(map(lambda item: item ** 2, my_list)))

# 2. List sorting by second element in the tuple
tup = [(0, 2), (4, 3), (9, 9), (10, -1)]
tup.sort(key=lambda x: x[1])
print(tup)
