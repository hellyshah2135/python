''' 47.  Write a Python function to check whether a number is in a given range Write a Python function to check whether a number is perfect or not'''

def check_range(number, start, end):
    if number in range(start, end + 1):
        return f"{number} is in the range [{start}, {end}]"
    else:
        return f"{number} is outside the range."
num = int(input("enter the number "))
start_range_num = int(input("enter the start range number "))
end_range_num = int(input("enter the end range number "))
print(check_range(num, start_range_num, end_range_num))