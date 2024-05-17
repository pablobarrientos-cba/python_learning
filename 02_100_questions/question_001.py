# Write a program which will find all such numbers
# which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def get_numbers_list():
    number_list = []
    for num in range(2000, 3201):
        if num % 7 == 0 and not num % 5 == 0:
            number_list.append(str(num))

    return number_list


def get_numbers_printed():
    for num in range(2000, 3201):
        if num % 7 == 0 and not num % 5 == 0:
            print(num, end=',')


def get_numbers_generator():
    print(* [num for num in range(2000, 3201) if num % 7 == 0 and not num % 5 == 0], sep=',')


# Solution 1, using a list
print(','.join(get_numbers_list()))

# Solution 2, printing directly in the for loop
get_numbers_printed()

# Solution 3, generator and list comprehension
print('\b')
get_numbers_generator()
