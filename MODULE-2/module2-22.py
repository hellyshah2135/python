''' 22. Write a Python program to check whether an element exists within atuple.
'''
import random
colors = ("Red", "Green", "Blue")

if random.choice(colors) in colors:
    print(f"Yes, {random.choice(colors)} is in the tuple.")