''' 14. Write a Python program to find the second smallest
number in a list.'''

def second_smallest(numbers):
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return "List needs at least two unique numbers"
    
    unique_numbers.sort()
    
    return unique_numbers[1]

print(second_smallest([1, 2, -8, -2, 0, -8])) 
