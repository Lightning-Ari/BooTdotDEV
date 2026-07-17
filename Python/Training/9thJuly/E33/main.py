from typing import Any
"""
Exercise 33. List to Dictionary Conversion

Practice Problem: Given two lists of the same length, 
one containing keys and the other containing values. combine them into a single dictionary.

Exercise Purpose: In data processing, you often receive related data in separate arrays. 
This exercise teaches you how to use the zip() function to pair elements and transform them into a dictionary.

Given Input:

    Keys: ["name", "age", "city"]
    Values: ["Alice", 25, "New York"]

Expected Output:

Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
"""
def dictionary_list(list_a: list[str], list_b: list[Any]) -> dict[str, Any]:
    return dict(zip(list_a, list_b))




keys_list: list[str] = ["name", "age", "city"]
values_list: list[Any] = ["Alice", 25, "New York"]

result: dict[str, Any] = dictionary_list(keys_list, values_list)

print(f"Dictionary: {result}")



