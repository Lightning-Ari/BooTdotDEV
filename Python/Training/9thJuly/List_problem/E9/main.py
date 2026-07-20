"""
Exercise 9. Create a Copy of a List
Practice Problem: Create a copy of an existing list so that modifying the copy does not change the original.

Exercise Purpose: This exercise addresses one of the most common “gotchas” for new Python programmers: Pass-by-Object-Reference. If you simply write list_b = list_a, both variables point to the same list in memory. Learning to “Clone” or “Copy” is vital for data integrity.

Given Input: Original: ["Apple", "Banana", "Cherry"]
"""
new_list: list[str] = ["Apple", "Banana", "Cherry"]

temp_list: list[str] = new_list[:]
print(f"Copy list is {temp_list} from {new_list}")

