''' 22. Write a Python program to get a string made of the first 2 and the last 2chars from a given a string. If the string length is less than 2, return instead of the empty string.
 o Sample String: w3resource' o
Expected Result: 'w3ce' o
SampleString: 'w3' o Expected
Result:
'w3w3' o Sample String: ' w' o
Expected Result: Empty String
'''

def string_both_ends(text):
    
    if len(text) < 2:
        return ""

    return text[:2] + text[-2:]

word = input("enter the word ")
result = string_both_ends(word)
print(f"the result of the text is {result}")
