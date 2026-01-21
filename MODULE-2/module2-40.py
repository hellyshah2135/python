'''Write a Python program to combine two dictionary adding
values forcommon keys.
 o d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200, ’d’:400}'''

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = Counter(d1) + Counter(d2)

final_dict = dict(result)

print(final_dict)
