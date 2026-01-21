''' 10. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero'''
ans = 0
def sum_three(a, b, c):
    
    if a == b or b == c or a == c:
        return 0
    return a + b + c

a = int(input("enter the value of a "))

b = int(input("enter the value of b "))

c = int(input("enter the value of c "))

ans= sum_three(a, b, c)

print(f"the sum of a, b and c is {ans}")




