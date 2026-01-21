''' 37.  Write a Python script to print a dictionary where the keys are numbersbetween 1 and 15.'''

numbers_dict = {x: x**2 for x in range(1, 16)}

print(numbers_dict)