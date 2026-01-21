''' 21. Write a Python function to reverses a string if its length is a
multiple of 4.'''

def reverse_string(word):
    if len(word) % 4 == 0:
        # Use string slicing to reverse the string
        # [start:stop:step] -> [::-1] means start to end, stepping backwards
        return word[::-1]
    else:
        return word
    
text = input("enter the text ")
reverse_text = reverse_string(text) 
print(f"the reversed text is {reverse_text}")