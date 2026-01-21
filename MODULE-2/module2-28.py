''' 28. Write a Python program to remove an empty tuple(s) from a list of tuples.'''

def remove_empty_tuples(list_of_tuples):
    
    result = [t for t in list_of_tuples if t]
    return result

data = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (''), ()]
clean_data = remove_empty_tuples(data)

print("Original List:", data)
print("Cleaned List:", clean_data)