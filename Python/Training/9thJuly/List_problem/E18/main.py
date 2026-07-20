"""
Practice Problem: Delete every instance of a specific value from a list.

Exercise Purpose: This is a Filtering Operation. A common mistake is using .remove(), which deletes only the first occurrence.
 To remove all instances, you need to filter the list. 
 This is essential for data scrubbing when you need to purge “bad data” or “flagged entries” entirely.

 Given Input:

    List: [5, 20, 15, 20, 25, 50, 20]
    Item to remove: 20

Expected Output: Cleaned List: [5, 15, 25, 50]
"""

new_list : list[int] = [5, 20, 20, 10, 15, 20, 25, 50, 20]

target: int = 20
temp_list: list[int] =[]

# Safe, fast, and works on all datasets
cleaned_list = [num for num in new_list if num != target]

#this is incorrect. this code will delete the item from the same list and skip some index
"""for num in new_list:
    if num == target:
        new_list.remove(target)"""

print(f"Cleaned List: {cleaned_list}")