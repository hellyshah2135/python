''' 17. Write a Python program to split a list into different variables'''

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

first, second, *others = fruits

print(first)  
print(second)
print(others) 