''' 7. Write a Python program to remove duplicates from a list.'''

# def remove_duplicates(input_list):
#     return list(set(input_list))

# my_list = [1, 2, 2, 3, 4, 4, 4, 5]
# print(remove_duplicates(my_list))


def remove_duplicates_ordered(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = ["apple", "banana", "apple", "orange", "banana"]
print(remove_duplicates_ordered(my_list))
