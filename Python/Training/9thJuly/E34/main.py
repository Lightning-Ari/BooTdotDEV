"""
Exercise 34. Find the Difference Between Two Lists

Practice Problem: Write a function that finds the “difference” between two lists—specifically, all elements that are present in the first list but not in the second list.

Exercise Purpose: This exercise explores Set Logic and exclusion. It is a common task when synchronizing databases or filtering out “already processed” items from a new batch of data.

Given Input:

    List A: [1, 2, 3, 4, 5]
    List B: [2, 4, 6]

Expected Output: Difference (A - B): [1, 3, 5]
"""
def difference_list1(list_a: list[int], list_b: list[int]) -> list[int]:
    set_b = set(list_b)  # Only convert the second list to a set
    
    # Keep the original order of list_a, but check against set_b instantly
    return [item for item in list_a if item not in set_b]


def difference_list(list_a: list[int], list_b: list[int]) -> list[int]:
    # Convert list_b to a set for O(1) fast lookups
    set_b = set(list_b)
    
    # Keep items from list_a if they are NOT in set_b
    # Wrapping it in list() satisfies the return type and maintains original order
    return list(set(list_a) - set(set_b))





list_a: list[int] = [1, 2, 3, 4, 5]
list_b: list[int]= [2, 4, 6]

result: list[int] = difference_list(list_a, list_b)

print(f"Difference (A - B): {result}")

