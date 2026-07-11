"""
Exercise 13. Access Nested Lists (Simple Indexing)
Practice Problem: Given a “list of lists,” access a specific item hidden inside the inner list.

Exercise Purpose: This exercise teaches you to navigate Multi-dimensional Data. Think of nested lists like a spreadsheet (Rows and Columns) or a theater seating chart. To find a specific seat, you need the row and seat numbers.

Given Input:

Nested List: [[1, 2], [3, 4, 5], [6, 7]]
Goal: Access the number 5.
"""

nested_list = [[1, 2], [3, 4, 5], [6, 7]]
print(f"{len(nested_list)}")

slice_list: list[int] = nested_list[1]
temp_list: list[int] = []

for sublist in nested_list:
    for item in sublist:
        temp_list.append(item)

print(f"{temp_list[4]}")

# Chain the indices: row index 1, column index 2
target_number = nested_list[1][2]
print(f"The number is: {target_number}")

