#Write a Python program to replace last value of tuples in a list.

list_of_tuples = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
new_value = 100

updated_list = [t[:-1] + (new_value,) for t in list_of_tuples]

print(updated_list) 
