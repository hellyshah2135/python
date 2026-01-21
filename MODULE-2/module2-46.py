# 46.  Write a Python function to calculate the factorial of a number (anonnegative integer)

def calculate_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
num = int(input("enter a number "))
print(calculate_factorial(num))