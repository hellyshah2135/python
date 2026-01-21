''' 11. Write a Python function that takes a list and returns a new list with unique elements of the first list.'''

def get_unique_elements(input_list):
    return list(set(input_list))

original = [15, 1, 2, 2, 3, 4, 4, 5, 1, 8, 15]
unique = get_unique_elements(original)
print(unique) 
