''' 17. Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.'''

# def swap_and_combine(str1, str2):
#     if len(str1) < 2 or len(str2) < 2:
#         return "Strings must have at least 2 characters."

    
#     new_str1 = str2[:2] + str1[2:]
#     new_str2 = str1[:2] + str2[2:]

#     return new_str1 + " " + new_str2

# string_a = input("enter first letter")
# string_b = input("enter second letter")

# result = swap_and_combine(string_a, string_b)
# print(f"Original: {string_a}, {string_b}")
# print(f"Result:   {result}")

def swap_and_combine(str1, str2):
    if len(str1)<2 or len(str2)<2:
        return "Strings must have at least 2 characters."
    
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    return new_str1 + " " + new_str2

string_a = input("enter first letter ")
string_b = input("enter second letter ")

result = swap_and_combine(string_a,string_b)
print(f"Original: {string_a}, {string_b}")
print(f"result : {result}")


