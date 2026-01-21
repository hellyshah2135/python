# 62. Write a Python program to find the maximum and minimum numbersfrom the specified decimal numbers.

from decimal import Decimal


numbers_list = [Decimal('1.55'), Decimal('0.05'), Decimal('10.25'), Decimal('5.75'), Decimal('0.01')]

max_val = max(numbers_list)
min_val = min(numbers_list)

print(f"Decimal Numbers: {numbers_list}")
print(f"Maximum Number: {max_val}")
print(f"Minimum Number: {min_val}")
