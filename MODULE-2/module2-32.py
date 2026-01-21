''' 32. Write a Python script to sort (ascending and descending) a dictionary byvalue.'''

data = {'apple': 50, 'banana': 10, 'cherry': 30}

asc = dict(sorted(data.items(), key=lambda item: item[1]))

desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", asc)  
print("Descending:", desc) 