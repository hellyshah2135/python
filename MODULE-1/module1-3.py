# 3. Write a Python program to get the Fibonacci series of given range

n = int(input("How many terms of the Fibonacci series do you want? "))

n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence:", n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1, end=" ")
        
        nth = n1 + n2
        n1 = n2
        n2 = nth
        
        count += 1