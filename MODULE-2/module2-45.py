''' 45.  Write a Python program to create a
dictionary froma string.o Note: Track the count of the letters from the string.Sample string:'w3resource'o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

from collections import Counter

sample_string = 'helly'

result_dict = dict(Counter(sample_string))

print("Character Count Dictionary:")
print(result_dict)

