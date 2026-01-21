#43. Write a Python program to find the highest 3 values in a dictionary

import heapq

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

highest_3 = heapq.nlargest(3, my_dict.values())

print("Highest 3 values:", highest_3)
