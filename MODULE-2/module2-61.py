# 61. Write a Python program to returns sum of all divisors of a number

def sum_divisors(n):
    total_sum = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            total_sum += i
            
    return total_sum

num = int(input("Enter a number: "))
print(f"The sum of all divisors of {num} is: {sum_divisors(num)}")