'''
50.How do you perform pattern matching in Python?

matching pattern in python is done by match case.

example:
command = "quit"
match command:
    case "start":
        print("System starting...")
    case "quit":
        print("System shutting down...")
    case _:
        print("Unknown command")

-----------------------------------------------------------


51. What is a Lambda Function?

A Lambda function is a small, anonymous function defined without a name using the lambda keyword

example:
square = lambda x: x * x
print(square(5)) # Output: 25

-----------------------------------------------------------


52. How Many Basic Types Of Functions Are Available In Python?

There are two basic types of functions:

Built-in Functions: Functions provided by Python itself, like print(), len(), max(), and type().

User-Defined Functions: Functions created by programmers using the def keyword to perform specific tasks.


-----------------------------------------------------------


53. How can you pick a random item from a list or tuple?

To use any of these, must first import random.
Pick a random item from a list or tuple?
Use random.choice().

example:
items = ['apple', 'banana', 'cherry']
print(random.choice(items))

-----------------------------------------------------------


54. How can you pick a random item from a range?

Use random.randrange(start, stop, step)
use random.randrange for range
--Picks a random even number between 0 and 10
print(random.randrange(0, 11, 2))


-----------------------------------------------------------


55. How can you get a random number in set?

use random.seed for set
--random.seed(10)
print(random.random()) # This will always output the same number now

-----------------------------------------------------------


56. How will you randomizes the items of a list in place?

use random.shuffle for list
--my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list) # The order is now scrambled


-----------------------------------------------------------


57. How will you set the starting value in generating random numbers?

import random

# Set the seed to a fixed number
random.seed(10)

print(random.random())   # Example Output: 0.5714025946899135
print(random.randint(1, 100)) # Example Output: 74

# If you run this script again with seed(10), 
# you will get 0.5714025946899135 and 74 every single time.


-----------------------------------------------------------
'''
