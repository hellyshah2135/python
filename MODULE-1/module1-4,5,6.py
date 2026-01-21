'''4. How is memory managed in Python?
Python manages memory automatically using two main mechanisms:

Reference Counting: Python keeps track of the number of references to an object. When an object's reference count drops to zero, the memory is deallocated.

Garbage Collection: To handle "reference cycles" (where two objects point to each other), Python has a cyclic garbage collector that periodically finds and deletes unreachable objects.

Private Heap Space: All Python objects and data structures are located in a private heap. The programmer does not have access to this heap; the Python interpreter manages it.

----------------------------------------------------------

5. What is the purpose of the continue statement?
The continue statement is used inside loops (for/while) to skip the current iteration and move immediately to the next one


----------------------------------------------------------


6. What are negative indexes and why are they used?
Negative indexes are used to access elements from the end of a sequence (like strings or lists).

-1 refers to the last item.

-2 refers to the second to last item. They are used because they provide a convenient way to access the end of a collection without needing to calculate the total length (e.g., list[len(list)-1]).

'''