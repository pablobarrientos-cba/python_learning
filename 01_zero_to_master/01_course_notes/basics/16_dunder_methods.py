# see reference https://docs.python.org/3/reference/datamodel.html#special-method-names
class Toy:
    def __init__(self, color):
        self.color = color

    def __str__(self):  # think about it as .ToString() in C#
        return f'I am a toy with {self.color} parts'


hally = Toy('purple')
print(str(hally))
