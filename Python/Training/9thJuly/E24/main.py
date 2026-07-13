"""
Exercise 24. Add New Item After a Specified Item

Practice Problem: Find a specific item in a list and insert a new item immediately after it.

Exercise Purpose: Unlike append() (end) or insert() (fixed index), this is a Context-Aware Insertion. This is useful for things like adding a “New!” tag after a specific product name or inserting a middleware step into a list of processing functions.

Given Input:

    List: [10, 20, 30, 40, 50]
    Insert after: 30
    New Item: 35

Expected Output: Updated List: [10, 20, 30, 35, 40, 50]
"""

original_list: list[int] = [10, 20, 30, 40, 50]
target: int = 30
new_value: int = 35
# updated_list: list[int] = [num for num in original_list if num]
updated_list: list[int] = []

for i in original_list:
    updated_list.append(i)
    if i == target:
        updated_list.append(new_value)

print(f"Updated List: {updated_list}")


# The Standard In-Place Solution (.index() and .insert())
original_list: list[int] = [10, 20, 30, 40, 50]
target: int = 30
new_value: int = 35

# Step 1: Find the current index of 30 (returns 2)
target_idx = original_list.index(target)

# Step 2: Insert 35 at index 3 (immediately after 30)
original_list.insert(target_idx + 1, new_value)

print(f"Updated List: {original_list}")
# Output: Updated List: [10, 20, 30, 35, 40, 50]



# An Advanced One-Line Solution (List Comprehension)
original_list: list[int] = [10, 20, 30, 40, 50]
target: int = 30
new_value: int = 35

# Advanced flattening syntax
updated_list = [
    x for num in original_list 
    for x in ([num, new_value] if num == target else [num])
]

print(f"Updated List: {updated_list}")
