'''7. Write python program that swap two number with temp
variable andwithout temp variable.'''

x = int(input("enter the value of x "))
y = int(input("enter the value of y "))


print(f"the value of x before swapping {x}")
print(f"the value of y before swapping {y}")

temp = x
x = y
y = temp

print(f"the value of x after swapping {x}")
print(f"the value of y after swapping {y}")