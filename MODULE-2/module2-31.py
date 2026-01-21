#31. How will you create a dictionary using tuples in python?

tuple_list = [("name", "helly"), ("age", 20), ("gender", "Female")]
dict_a = dict(tuple_list)

keys = ("a", "b", "c")
values = (1, 2, 3)
dict_b = {keys[i]: values[i] for i in range(len(keys))}

print(dict_a)