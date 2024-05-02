import sys
from random import randint

print(sys.argv)

low_limit = 1 if not sys.argv else sys.argv[0]
up_limit = 10 if not sys.argv else sys.argv[1]

print('========== WELCOME TO THE GUESSING GAME========')
print(f"Number to guess between {low_limit} and {up_limit}")
number_to_guess = randint(low_limit, up_limit)
print(number_to_guess)
