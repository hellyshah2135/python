# 41. Write a Python program to print all unique values in a dictionary.

data = {
    "V": "S001", "V1": "S002", "VI": "S001", 
    "VI1": "S005", "VII": "S005", "V2": "S009", "VIII": "S007"
}

unique_values = set(data.values())

print("Unique Values:", unique_values)
