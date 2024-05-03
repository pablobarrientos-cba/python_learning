# Keys can be anything as long as it is immutable
# Keys needs to be unique, if duplicate, the value is overwritten

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'is_veteran': True,
    'greet': 'see you later',
    87: 'Los piojos',
    True: 'Allowed',
    (3.45, 52.87): "Pittsburgh"
}
# Accessing a non-existing key is possible without error.
# It returns None, and we can default the value
# user.get('has_gun', True)

print(user.get('greet'))
print(user.get('has_gun', True))
print(user.get(87))
print(user.get(True))
print(user.get((3.45, 52.87)))

print('greet' in user.keys())
print('Allowed' in user.values())
