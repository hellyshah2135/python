''' 12. Write a Python program to convert a list of characters into a string.'''

def list_to_string(char_list):
    result_string = "".join(char_list)
    return result_string

characters = ['H', 'e', 'l', 'l', 'y']
word = list_to_string(characters)

print(f"List: {characters}")
print(f"String: {word}") 
