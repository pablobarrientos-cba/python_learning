class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class Garfield(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all the pets (create 3 cat instances from the above)
simon = Simon('Simon', 1)
sally = Sally('Sally', 1)
garfield = Garfield('Garfield', 1)
my_cats = [simon, sally, garfield]

# 3 Instantiate the Pet class with all your cats use variable my_pets
pets = Pets(my_cats)

# 4 Output all the cats walking using the my_pets instance
pets.walk()
