''' 13. Selecting an Item Randomly from a List'''

import random

def pick_random_item(my_list):
    if not my_list:
        return "List is empty!"
    
    return random.choice(my_list)

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
random_color = pick_random_item(colors)

print(f"The computer picked: {random_color}")