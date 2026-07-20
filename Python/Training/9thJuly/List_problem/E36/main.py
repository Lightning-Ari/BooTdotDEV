"""
Exercise 36. Extend Nested List by Adding a Sublist
Practice Problem: Write a function that iterates through a list of nested lists and appends a specific sublist (or value) to each inner list.

Exercise Purpose: Working with “lists of lists” is common in matrix manipulation and data grouping. This exercise reinforces the concept of Nested Iteration, accessing an object that exists inside another object and modifying it in place.

Given Input:

Nested List: [['apple', 'banana'], ['cherry', 'date']]
To Append: "elderberry"
Expected Output: Modified List: [['apple', 'banana', 'elderberry'], ['cherry', 'date', 'elderberry']]
"""

def list_append(list_a: list[list[str]], target_value: str) -> list[list[str]]:
    return [sublist + [target_value] for sublist in list_a]

original_list: list[list[str]] = [['apple', 'banana'], ['cherry', 'date']]
target: str = "elderberry"

new_list: list[list[str]] = list_append(original_list, target)


print(f"Modified List: {new_list}")