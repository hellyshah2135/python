''' 6. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a givenlist of strings'''

def count_special_strings(words):
    count = 0
    
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
            
    return count

sample_list = ['abc', 'xyz', 'aba', '1221', 'bhg', 'a']
result = count_special_strings(sample_list)

print(f"Total count: {result}")