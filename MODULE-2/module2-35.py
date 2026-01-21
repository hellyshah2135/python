''' 35. How Do You Traverse Through A Dictionary Object In Python?
'''

user = {"name": "Alice", "role": "Admin", "id": 501}

for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f"{key}: {value}")