''' 16. Write a Python program to check whether a list contains a sub list'''

list_str = str([1, 2, 3, 4])[1:-1] 
sub_str = str([2, 3])[1:-1]      

if sub_str in list_str:
    print("Sublist found!")