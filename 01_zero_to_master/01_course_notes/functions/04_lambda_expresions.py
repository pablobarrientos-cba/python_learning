# Lambda expressions are anonymous functions that I need to execute only once
# structure -> lambda param/params: param manipulation

from functools import reduce

my_list = [1, 2, 3]
double_list = list(map(lambda item: item * 2, my_list))
print(double_list)

scores = [40, 55, 70, 87, 90, 100]
approved = list(filter(lambda score: score >= 70, scores))
print(approved)

total = reduce(lambda acc, item: acc + item, my_list)
print(total)
