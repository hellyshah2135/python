''' 49. Write a Python function that checks whether a passed string is palindromeor not
'''
def is_palindrome(text):
    clean_text = "".join(char.lower() for char in text if char.isalnum())
    
    return clean_text == clean_text[::-1]


test_strings = ["madam", "nurses run", "hello", "A man, a plan, a canal: Panama"]

for s in test_strings:
    print(f"'{s}' is a palindrome: {is_palindrome(s)}")
