''' 14.Write a Python program to count the number of characters (characterfrequency) in a string
'''
def count_char_frequency(input_string):
    frequency_dict = {}
    
    for char in input_string:
        
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
            
    return frequency_dict

sample_text = input("enter the text")
result = count_char_frequency(sample_text)
print(result)