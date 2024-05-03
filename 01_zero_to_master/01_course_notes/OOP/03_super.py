class Person:
    def __init__(self, dni):
        self.dni = dni


class Student(Person):
    def __init__(self, dni, career):
        super().__init__(dni)
        self.carer = career


paul = Student(34, 'data science')
print(paul.dni)
print(paul.carer)
