"""
Exercise 19. Remove Empty Strings from a List of Strings

Practice Problem: Take a list of strings that contains empty entries ("") and remove them to keep only the valid text.

Exercise Purpose: Real-world data is often “noisy.” When you split a paragraph into words or import a CSV, you often end up with empty strings. Learning to “sanitize” your lists is a daily task for developers and data scientists.

Given Input: List: ["Mike", "", "Emma", "Kelly", "", "Brad"]

Expected Output: Cleaned Names: ['Mike', 'Emma', 'Kelly', 'Brad']
"""

new_list: list[str] = ["Mike", "", "Emma", "Kelly", "", "Brad"]
clean_list: list[str] = [name for name in new_list if name != ""]

print(f"Cleaned Names: {clean_list}")

"""
While your solution is excellent, you can make the if condition even shorter.
 In Python, an empty string "" evaluates to False in a boolean context (this is called a "Falsy" value).
 Any string with text evaluates to True ("Truthy").
"""
second_list: list[str] = [name for name in new_list if name]
print(f"Cleaned Names: {second_list}")