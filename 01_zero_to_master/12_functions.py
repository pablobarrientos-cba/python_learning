# parameters
# default parameters
def say_hello(name='Gandalf', emoji='#'):
    """
    Print a friendly message
    :param name: The name we need to greet
    :param emoji: The emoji we add ti the greeting
    """
    print(f'hello {name} - {emoji}')


# arguments (positional)
say_hello('Pablo', '*')
say_hello('Andrew')
say_hello()

# keyword arguments
say_hello(emoji='***', name='Aragorn')


# *args / **kwargs
def super_func(*args, **kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, n2=10))
