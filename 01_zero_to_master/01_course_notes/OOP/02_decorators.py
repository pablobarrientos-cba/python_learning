class Person:
    species = 'human'  # class attribute

    def __init__(self, name, age):  # init method or constructor method
        self.name = name
        self.age = age

    def say_hello(self):  # instance method can access both class and instances attributes
        print(f'Hello, my name is: {self.name} I belong to {self.species} race')

    @classmethod  # requires cls param and can access only to class attributes
    def need_sleep(cls, hours):
        print(f'{cls.species} need to sleep {hours} hours')

    @staticmethod
    def feed():
        print(f'Feed')

    def return_self(self):
        return self


paul = Person('Paul', 47)

# how self works
print(paul)
print(paul.return_self())

# instance methods
paul.say_hello()
paul.need_sleep(5)
paul.feed()

# class methods
# not possible Person.say_hello()
Person.need_sleep(5)
Person.feed()
