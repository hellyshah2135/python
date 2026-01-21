''' 4. Write a Python function to get the largest number, smallest num and sumof all from a list.'''

def get_list_stats(numbers):
    if not numbers:
        return None, None, 0
    
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    
    return largest, smallest, total_sum

my_list = [15, 2, 45, 10, 33]
high, low, total = get_list_stats(my_list)

print(f"Largest: {high}") 
print(f"Smallest: {low}") 
print(f"Total Sum: {total}")


''' 5. How to Compare Two Lists

there are several ways to compare lists:

(a) using '==' to check for equality

(b) using 'is' to check for memory location

(c) using '&' to check for common elements

(d) using '-' to check for elements which are in list1 but not in list2 

(e) using '^' to check for non-common elements

(f) using '<' or '>' to check the if the first element is same than it moves forward and so on
'''