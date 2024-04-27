# List slicing
amazon_cart = [
    'Notebooks',
    'Sunglasses',
    'Harry Potter Book',
    'Over grip'
]
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0:4])
print(amazon_cart[0:4:2])

# Matrix 2D Arrays
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][1])  # prints 5
for row in matrix:
    print(row)
    print(row[1])

# list methods
# Adding
basket_items = [1,2,3]
print(f"{basket_items =} original")

basket_items.append(4)
print(f"{basket_items =} appending")

basket_items.insert(0, 0)
print(f"{basket_items =} inserting leading 0")

basket_items.extend([5,6,7])
print(f"{basket_items =} extending")

# Removing
basket_items.pop()
print(f"{basket_items =} last element removed")

basket_items.pop(0)
print(f"{basket_items =} element removed by index")

basket_items.remove(3)
print(f"{basket_items =} element removed by value")

basket_items.clear()
print(f"{basket_items =} after clear")

# sorting and counting
letters = ['a','x','b','n','c','x']
print(f"{letters =}")
print(f"x can be found {letters.count('x')} times")

letters.sort()
print(f"{letters =} sorted")

letters.sort(reverse=True)
print(f"{letters =} reverse sorted")


