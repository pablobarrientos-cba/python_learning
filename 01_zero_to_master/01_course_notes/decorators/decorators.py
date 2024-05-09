def decorator_structure(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper()  # make sure to return as variable


def enhanced_message(func):
    def wrapper(*args, **kwargs):
        print('*********************')
        result = func(*args, **kwargs)
        print('*********************')
        return result
    return wrapper


@enhanced_message
def say_morning(name, gender, age):
    print(f'Good Morning {name}!')


@enhanced_message
def say_later(name, emoji):
    print(f'Ok {name} See you later! / {emoji}')


say_morning('Pablo', 2, 3)
say_later('Silvana', ':p')
