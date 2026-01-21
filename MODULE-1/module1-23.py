''' 23. Write a Python function to insert a string in the middle of a string'''

def insert_string_middle(original, to_insert):
    middle = len(original) // 2
    
   
    return original[:middle] + " " + to_insert + original[middle:]


main_string = input("enter the main string ")
add_string = input("enter the add string ")
result = insert_string_middle(main_string,add_string)

print (f"the resulted string value is : {result}")

