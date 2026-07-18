"""
Exercise 35. Remove Negative Numbers In-place

Practice Problem: Write a function that removes all negative numbers from a list without creating a new list. You must modify the original list object directly.

Exercise Purpose: This is a classic “trap” exercise. If you remove items while iterating forward, the indices shift and you will skip elements. This exercise teaches In-place Modification and the importance of iterating backwards or using slice assignment.

Given Input: List: [10, -5, 20, -1, 0, -8]

Expected Output: Modified List: [10, 20, 0]
"""
def remove_negative(list_a: list[int]) -> list[int]:
    return [num for num in list_a if num >= 0]



original_list: list[int] = [10, -5, 20, -1, 0, -8]


result: list[int] = remove_negative(original_list)
print(f"Modified List: {result}")

#hello