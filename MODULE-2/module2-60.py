# 60.  Write a Python program to calculate surface volume and area of acylinder

import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = math.pi * radius**2 * height
surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")