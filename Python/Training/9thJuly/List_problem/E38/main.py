"""
Exercise 38. Flatten Nested List (2D to 1D)
Practice Problem: Take a 2D list (a list containing several lists) and “flatten” it into a single 1D 
list containing all the individual elements in their original order.

Exercise Purpose: Flattening is a core data-wrangling task. 
When you have data chunked into groups (like rows in a table) but need to perform a single operation on every individual piece, 
you must flatten the structure first.

Given Input: 2D List: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

Expected Output: 1D List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

original_list: list[list[int]] = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

result: list[int] = [b for a in original_list for b in a ]

print(f"1D List: {result}")

result1 = sum(original_list, [])

print(f"1D List: {result1}")