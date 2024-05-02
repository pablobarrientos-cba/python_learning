def highest_even(*args):
    max_even = 0
    for num in args:
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even


def highest_even_v2(*args):
    evens = []
    for num in args:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)


print(highest_even(1, 3, 5, 7, 2, 7))
print(highest_even_v2(1, 3, 5, 7, 10, 7))
