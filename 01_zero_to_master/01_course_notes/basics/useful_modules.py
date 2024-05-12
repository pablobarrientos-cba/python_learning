from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

intArray = array('i', {3, 94, 57, 56, 37, 83, 9, 0, 1, 2, -2})
print(intArray[0])
print(intArray)

print(datetime.date.today())

phrase = 'This is a test and blah blah blah'
print(Counter(phrase))

d = defaultdict(lambda: 87, dict(a=1, b=2))
print(d['a'])  # returns 1
print(d['x'])  # returns default 87

d1 = {1: 1, 2: 2, 3: 3}
d2 = {2: 2, 3: 3, 1: 1}
print(d1 == d2)  # returns True

# Ordered Dictionary store and keep track of the insertion order
od1 = OrderedDict(d1)
od2 = OrderedDict(d2)
print(od1 == od2)  # returns False
