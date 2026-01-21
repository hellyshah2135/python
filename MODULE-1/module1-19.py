''' 19. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole'not'...'poor'substring with 'good'. Return the resulting string.'''

def treat_string(text):
    index_not = text.find('not')
    index_poor = text.find('poor')

    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        text = text[:index_not] + 'good' + text[index_poor + 4:]
        return text
    else:
        return text
    
sentence = input("enter the sentence ")  
result = treat_string(sentence)  

print(f"the result : {result}")