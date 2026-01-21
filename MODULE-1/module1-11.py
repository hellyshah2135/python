''' 11. Write a Python program that will return true if the
two given integer values are equal or their sum or
difference is 5.
'''

def check_values(x, y):
    if x == y or (x + y) == 5 or (x - y) == 5:
        return True
    else:
        return False

print(f"5 and 5: {check_values(5, 5)}")      
print(f"2 and 3: {check_values(2, 3)}")     
print(f"7 and 2: {check_values(7, 2)}")     
print(f"1 and 2: {check_values(1, 2)}") 

