''' 48. Write a Python function that checks whether a Number is Perfect or not'''

def is_perfect(n):
    if n <= 0:
        return False
    
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
            
    return sum_divisors == n

num = int(input("enter a number "))
if is_perfect(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")