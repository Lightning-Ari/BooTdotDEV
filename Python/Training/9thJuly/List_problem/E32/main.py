"""
Exercise 32. Check if List is Sorted

Practice Problem: Create a function that determines if a list of numbers is sorted in non-decreasing (ascending) order. 
Return True if it is, and False otherwise.

Exercise Purpose: Checking order is a common prerequisite for algorithms like Binary Search. This exercise teaches you to perform Neighbor Comparison by examining an element and its immediate successor together.

Given Input: List: [10, 20, 30, 25, 40]

Expected Output: Is Sorted: False
"""
def sort_fun(numbers: list[int]) -> bool:
    return sorted(numbers, reverse= False) == numbers

original_list: list[int] = [10, 20, 30, 25, 40]
result: bool = sort_fun(original_list)

print(f"Is Sorted: {result}")
