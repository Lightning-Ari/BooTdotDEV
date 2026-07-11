"""
Exercise 12. Swap Two Elements at Given Indices
Practice Problem: Write a script to swap the positions of two elements in a list based on their indices.

Exercise Purpose: Swapping is the heart of every sorting algorithm like Bubble Sort or Quick Sort. While other languages require a temporary variable to hold a value during the swap, Python offers an elegant, one-line tuple unpacking method that is faster to write and less error-prone.

Given Input:

List: [23, 65, 19, 90]
Indices to Swap: 0 and 2
"""

new_list: list[int] = [23, 65, 19, 90]
temp_data: int = new_list[0]
new_list[0] = new_list[2]
new_list[2] = temp_data

print(f"The new list is {new_list}")

second_list: list[int] = [23, 65, 19, 90]
pos1: int = 0
pos2: int = 2

second_list[pos1], second_list[pos2] = second_list[pos2], second_list[pos1]

print(f"new list {second_list}")

