"""
Exercise 25. Replace List's Item with New Value if Found

Practice Problem: Find the first occurrence of a specific value in a list and replace it with a new value.

Exercise Purpose: This is a Selective Update. 
It mimics “Find and Replace” functionality. 
It teaches you how to identify a location in memory and overwrite it without affecting the rest of the list structure.

Given Input:

    List: [5, 10, 15, 20, 25]
    Find: 20
    Replace with: 200

Expected Output: Modified List: [5, 10, 15, 200, 25]
"""
original_list: list[int] = [5, 10, 15, 20, 25]
target: int = 20
new_value: int = 200
modified_list: list[int] = original_list[:]

if target in original_list:
    # find the index for target
    target_indx: int = original_list.index(target)
    #update new value to modified list
    modified_list[target_indx] = new_value
else : 
    raise Exception("invalid target given")


#print new list
print(f"Modified List: {modified_list}")