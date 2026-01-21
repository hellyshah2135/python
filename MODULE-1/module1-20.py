''' 21. Write a Python function that takes a list of words and returns the length ofthe longest one.'''

def find_longest_word_length(word_list):
    max_length = 0
    
    for word in word_list:
       
        if len(word) > max_length:
            max_length = len(word)
            
    return max_length


words = ["PHP", "Exercises", "Backend", "Python"]
print(f"The length of the longest word is: {find_longest_word_length(words)}")
