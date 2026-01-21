''' 34. Write a Python script to check if a given key already exists in adictionary.'''

def check_key_existence(data_dict, key_to_check):
    if key_to_check in data_dict:
        print(f"Key '{key_to_check}' exists! Value: {data_dict[key_to_check]}")
    else:
        print(f"Key '{key_to_check}' does not exist.")

student_data = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science"
}

check_key_existence(student_data, "age")     
check_key_existence(student_data, "grade")   