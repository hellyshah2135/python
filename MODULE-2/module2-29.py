''' 29. Write a Python program to unzip a list of tuples into individual'''

list_of_tuples = [('Apple', 5), ('Banana', 12), ('Cherry', 8)]

names, quantities = map(list, zip(*list_of_tuples))

print("Names:", names)
print("Quantities:", quantities)

