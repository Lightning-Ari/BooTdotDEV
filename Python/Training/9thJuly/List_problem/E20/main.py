"""
Exercise 20. Remove Duplicates from List

Practice Problem: Remove all duplicate values from a list while keeping only one instance of each element.

Exercise Purpose: This exercise introduces Set Theory. In programming, you often need to ensure uniqueness (e.g., a list of unique email subscribers). While there are many ways to do this, using Python’s set or dict structures is the fastest way to handle the logic.

Given Input: List: [10, 20, 10, 30, 40, 40, 20, 50]

Expected Output: Unique List: [10, 20, 30, 40, 50]
"""

new_list: list[int] = [10, 20, 10, 30, 40, 40, 20, 50]
uniqu_list: list[int] = list(dict.fromkeys(new_list))

print(f"Unique list: {uniqu_list}")

"""
"To remove duplicates while preserving the list's original order, 
I used dict.fromkeys(). While casting to a set is faster to write, 
sets are unordered and will scramble the data. Using dictionary keys 
ensures uniqueness while maintaining sequence order at optimized C-speed under the hood."
"""