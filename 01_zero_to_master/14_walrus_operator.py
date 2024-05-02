walrus = 'walrus operator'

if (length := len(walrus)) > 10:
    print(f'Length is {length}')

while (length := len(walrus)) > 1:
    print(length)
    walrus = walrus[:-1]

print(walrus)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
