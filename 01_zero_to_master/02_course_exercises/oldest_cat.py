# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
tom = Cat('Tom', 2)
kitty = Cat('Kitty', 3)
horus = Cat('Horus', 5)


# 2 Create a function that finds the oldest cat
def oldest_age(*age_list):
    return max(age_list)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
age = oldest_age(tom.age, kitty.age, horus.age)
print(f'The oldest cat is {age} years old')
