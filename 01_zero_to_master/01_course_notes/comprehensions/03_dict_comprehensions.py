sample_dict = {
    'a': 3,
    'b': 4
}
my_dict = {k: v ** 2 for k, v in sample_dict.items() if v % 2 == 0}
print(my_dict)

my_dict = {num: num ** 2 for num in [1, 2, 3]}
print(my_dict)

# my_dict = {k:v for v[0], v[1] in [('a', 1), ('b', 2)]}
