''' 18. Write a Python program to add 'ing' at the end of a given string (lengthshould be at least 3). If the given string already ends with 'ing' then add'ly' instead if the string length of the given string is less than 3, leave it unchanged.
'''

def modify_string(text):

    if len(text) < 3:
        return text
    
    if text.endswith('ing'):
        text += 'ly'
    else:
        text += 'ing'

    return text

sentence = input("enter the sentence")
result = modify_string(sentence)

print(f"modified string is {result}")