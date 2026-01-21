''' 1.What is a List? How will you reverse it?

In Python, a List is a versatile, ordered collection of items. Think of it like a container that can hold different types of data (integers, strings, or even other lists) in a specific sequence.

A list is defined using square brackets []. It is mutable, meaning you can change its contents after it has been created.

How to reverse a list: There are two primary ways to do this depending on whether you want to modify the original list or create a new one.

list.reverse(): This reverses the list in-place (it changes the original list and returns None).

Slicing [::-1]: This creates a new reversed list and leaves the original one unchanged. 


-----------------------------------------------------------


2. How will you remove the last object from a list?

You use the .pop() method. By default, .pop() removes and returns the last item in the list.


-----------------------------------------------------------


3. If list1 is [2, 33, 222, 14, 25], what is list1[-1]?

In Python, negative indexing starts from the end of the list. list1[-1] is 25.


-----------------------------------------------------------


4. Differentiate between append() and extend()

append(item) --> Adds the object as a single entity to the end of the list.

extend(iterable) --> Iterates over the input and adds each element individually.
'''