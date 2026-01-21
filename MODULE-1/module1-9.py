''' 9. Write a Python program to test whether a passed letter is a vowel or not.'''

char = input("Enter a letter: ").lower()
if char in 'aeiou':
    print("It is a vowel")
else:
    print("It is a consonant")