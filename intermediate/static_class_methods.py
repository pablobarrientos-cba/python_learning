# Static and Class Methods.
# Class Methods: need cls param
# Static method can be executed at class level

class person:
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_population(cls):
        return cls.population

    def display(self):
        print(self.name, 'is', self.age, "years old.")


def is_adult(age):
    return age >= 18


newPerson = person("Pablo", 48)
is_adult(45)
newPerson.display()

print(person.get_population())


