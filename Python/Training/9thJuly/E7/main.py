"""
Exercise 7. Reverse a List
Practice Problem: Take a list and reverse the order of its elements.

Exercise Purpose: Reversal is a fundamental operation in data structures (like reversing a string or a linked list). Python provides multiple ways to do this, and understanding the difference between In-place Reversal (changing the original) and Slicing (creating a new one) is crucial for memory management.

Given Input: List: [100, 200, 300, 400, 500]

Expected Output: Reversed List: [500, 400, 300, 200, 100]
"""

new_list: list[int] = [100, 200, 300, 400, 500]
list_data: list[int] = new_list[:]
new_list.reverse()
print(f"the reverse list is {new_list} from the list {list_data}")