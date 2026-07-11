"""
Exercise 11. List Slicing: Extract Middle Elements
Practice Problem: Given a list, extract a “slice” containing the middle three elements.

Exercise Purpose: Slicing is one of Python’s most powerful features. Unlike many languages that require manual loops to copy array sub-sections, Python uses [start:stop] syntax. This forms the foundation for data windowing and pagination in web development.

Given Input: List: [10, 20, 30, 40, 50, 60, 70]

Expected Output: Middle Three: [30, 40, 50]
"""

new_list: list[int] = [10, 20, 30, 40, 50, 60, 70]
slice_list: list[int] = new_list[2:5]

print(f"The slices list is {slice_list} from the list {new_list}")