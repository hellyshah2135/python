# 58. Write a Python program to calculate the area of a trapezoid 

base_1 = float(input("Enter the length of the first base (a): "))
base_2 = float(input("Enter the length of the second base (b): "))
height = float(input("Enter the height (h): "))

area = ((base_1 + base_2) / 2) * height

print(f"The area of the trapezoid is: {area}")