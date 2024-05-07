some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in some_list:
    if value not in duplicates and some_list.count(value) > 1:
        duplicates.append(value)

# Turn a 1 line code using comprehensions
dup = list({item for item in some_list if some_list.count(item) > 1})
print(dup)
