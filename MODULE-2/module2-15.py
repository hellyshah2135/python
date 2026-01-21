''' 15. Write a Python program to get unique
values from a list'''

def get_unique_values(data_list):
   
    return list(set(data_list))

my_list = [10, 20, 10, 30, 40, 20, 50]
print(get_unique_values(my_list))
