from typing import Any

"""
Exercise 2. Perform List Manipulation
Practice Problem: Take a given list and modify it through five specific actions:

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 to the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
Exercise Purpose: Python lists are mutable, meaning they can be changed after they are created. 
This exercise demonstrates the various ways to “reshape” your data dynamically during execution.

Given Input: Initial List: [100, 50, 400, 500]
"""

#starting with a list
new_list: list[Any] = [100, 50, 400, 500]
print("Starting with default list")
print(f"{new_list}\n")


#updating 2nd element
new_list[1] = 200
print(f"Updating list 2nd element to 200 \n{new_list} \n")


#appending elemetn 600 to the list
new_list.append(600)
print(f"Appanded 600 to the end of the list.\n{new_list} \n")

#addling 300 to 3 position to the list
new_list.insert(2, 300)
print(f"Inserting 300 to 3rd position\n{new_list}\n")

#Removing by value
new_list.remove(600)
print(f"Removing by value 600\n{new_list}\n")

#Removing by index
del new_list[0]
print(f"Removing value by index 0\n{new_list}")






