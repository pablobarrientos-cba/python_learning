class Person:
    pass


# instances
paul = Person()
pete = Person()


class PlayerCharacter:
    def __init__(self, name): #  init method or constructor
        self.name = name

    def run(self):
        print(f'{self.name} is running')


player1 = PlayerCharacter('Gandalf')
player1.run()
