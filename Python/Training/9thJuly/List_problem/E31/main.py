"""
Exercise 31. Filter Strings by Length in a List

Practice Problem: Write a function that takes a list of strings and an integer k. 
The function should return a new list containing only the strings that have a length greater than or equal to k.

Exercise Purpose: This exercise introduces List Comprehensions, which are the “Pythonic” way to filter data. 
It demonstrates how to combine iteration and conditional logic into a single, readable line of code.

Given Input:

    List: ["apple", "pie", "banana", "kiwi", "pear"]
    k: 5

Expected Output: Filtered List: ['apple', 'banana']
"""

def filter_str(names: list[str], pos: int) -> list[str]:
    return [word for word in names if len(word) >= pos]


original_list: list[str] = ["apple", "pie", "banana", "kiwi", "pear"]
target: int = 5

result: list[str] = filter_str(original_list, target)
print(f"Filtered List: {result}")