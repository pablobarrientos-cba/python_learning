# for
# we know in advance the amount of iterations
# SYNTAX: for <var> in range(<begin>, <end>):
# powerful to act as a foreach. See example below

for i in range(4):
    print (i) # 0, 1, 2, 3
print ("\n")

for i in range(0, 4):
    print (i) # 0, 1, 2, 3
print ("\n")

for i in range(2, 4):
    print (i) # 2,3
print ("\n")

for char in "Pablo":
    print(char)
print("\n")

# Act as foreach
numbers = [1,2,3,4,5,6]
for num in numbers:
    print(num)
    print(num + 10)