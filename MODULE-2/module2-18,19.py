''' 18. What is tuple? Difference between list and tuple.

Tuple is a collection of items that is ordered and immutable.() brackets are used to write the elements in tuple.

Feature      List ([])                  Tuple (())

Mutability	 Mutable: You can add,      Immutable: Once 
             remove, or                 created, it 
             change items.	            cannot be changed.

Performance  Slower (requires more      Faster: More memory
             memory overhead).          -efficient for  
                                        fixed data.

Methods     Many methods (append,       Only two methods
            pop, sort, etc.).           (count, index)
'''

#Write a Python program to create a tuple with different datatypes.

mixed_tuple = (
    "helly", 2026, 3.14, True, [1, 2, 3], ("A", "B")      
)

print("The Mixed Tuple:", mixed_tuple)

print("\nElement Types:")
for item in mixed_tuple:
    print(f"Value: {item}  Type: {type(item)}")
