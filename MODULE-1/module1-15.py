''' 15. Write a Python program to count occurrences of a substring in a string.
'''

def count_string(main_string, sub_string):
    return main_string.count(sub_string)

text= "The quick brown fox jumps over the lazy dog. The fox is clever."
search = "fox"

result = count_string(text,search)
print(f"the {search} appears {result} times")