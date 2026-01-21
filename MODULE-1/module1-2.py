# 2. Write a Python program to get the Factorial number of given number

number = int(input(f"enter a number"))
factorial=1
for i in range(1,number+1):
    factorial*=i
print(f"factorial of {number} is {factorial}")
