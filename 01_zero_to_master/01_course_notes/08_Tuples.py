# Tuples are immutable sequences, typically used to store collections
# of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in).
# Tuples are also used for cases where an immutable sequence
# of homogeneous data is needed (such as allowing storage in a set or dict instance).

my_tuple = (1, 2, 3, 4, 3, 4, 3, 5, 3)
print(2 in my_tuple)

print(my_tuple.count(3))  # how many times in the series
print(my_tuple.index(3))  # return first occurrence index
