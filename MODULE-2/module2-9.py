''' 9. Finding Common Members Between Two Lists'''

def have_common_member(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    if (set1 & set2):
        return True
    else:
        return False

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]
list_c = [10, 11, 12]

print(f"A and B share items: {have_common_member(list_a, list_b)}") 
print(f"A and C share items: {have_common_member(list_a, list_c)}")