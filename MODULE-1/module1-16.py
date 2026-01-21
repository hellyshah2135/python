''' 16. Write a Python program to count the occurrences of each word in a givensentence
'''

def count_word_frequency(sentence):
    words = sentence.lower().split()
     
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

text = input("enter the sentence")
result = count_word_frequency(text)

for word, count in result.items():
    print(f"{word} : {count}")



