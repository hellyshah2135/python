''' 27. • Write a Python program to find the repeated items of a tuple.'''

def find_repeated(my_tuple):
    seen = set()
    repeated = []
    
    for item in my_tuple:
        if item in seen:
            if item not in repeated:
                repeated.append(item)
        else:
            seen.add(item)
            
    return repeated

numbers = (1, 2, 3, 2, 4, 5, 6, 2, 1, 21, 21)
print("Repeated items:", find_repeated(numbers))
