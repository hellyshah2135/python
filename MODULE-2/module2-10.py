''' 10.  Write a Python program to generate and print a list of first and last 5elements where the values are square of numbers between 1 and 30.'''

def generate_squares():
    squares = [x**2 for x in range(1, 31)]
    
    first_five = squares[:5]
    
    last_five = squares[-5:]
    
    print("First 5 squares:", first_five)
    print("Last 5 squares:", last_five)

# Run the program
generate_squares()