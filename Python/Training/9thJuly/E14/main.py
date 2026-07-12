"""
Exercise 14. Check if List Contains a Specific Item
Practice Problem: Write a check to see if a certain value exists within a list and print a message based on the result.

Exercise Purpose: This is a Membership Test. It’s the logic used for “Is this username taken?” or “Is this item in the shopping cart?” Python’s in operator makes this incredibly readable, almost like plain English.

Given Input:

Inventory: ["Laptop", "Mouse", "Monitor", "Keyboard"]
Target: "Tablet"
Expected Output: Is Tablet in inventory? False
"""
items: list[str] = ["Laptop", "Mouse", "Monitor", "Keyboard"]
result: bool = False 
for item in items:
    if item == "Tablet":
        result = True
    
print(f"Is Tablet in inventory? {result}")

items: list[str] = ["Laptop", "Mouse", "Monitor", "Keyboard"]
target: str = "Tablet"

# The 'in' operator automatically returns True or False
result: bool = target in items

print(f"Is {target} in inventory? {result}")
# Output: Is Tablet in inventory? False

