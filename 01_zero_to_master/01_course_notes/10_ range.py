# range is a function or special object in Python

for num in range(10):
    print(num)

for _ in range(0, 10):   # _ is the anonymous variable name
    print(_)

for _ in range(10, 0, -1):  # it gets a reverse range
    print(_)

for _ in range(2):  # it gets a list of integer in the range specified, twice
    print(list(range(10)))
