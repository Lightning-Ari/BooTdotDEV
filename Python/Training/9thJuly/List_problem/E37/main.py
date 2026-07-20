"""
Exercise 37. Concatenate Two Lists in a Specific Order
Practice Problem: Given two lists of strings, 
create a new list that contains every possible combination of elements from the first and second list, concatenated together.

Exercise Purpose: This exercise simulates a Cartesian Product. 
It is useful for generating permutations like combining first names with last names or product categories with sizes. 
It shows how Nested List Comprehensions can replace bulky nested loops.

Given Input:

List 1: ["Hello ", "Take "]
List 2: ["Dear", "Sir"]
Expected Output:

Result: ['Hello Dear', 'Hello Sir', 'Take Dear', 'Take Sir']
"""

def concatenate_list(list_a: list[str], list_b: list[str])-> list[str]:
    return [a + b for a in list_a for b in list_b]

list_1: list[str] = ["Hello ", "Take "]
list_2: list[str] = ["Dear", "Sir"]

list_3: list[str] = concatenate_list(list_1, list_2)

print(f"Result: {list_3}")



from itertools import product

def concatenate_list1(list_a: list[str], list_b: list[str]) -> list[str]:
    return [a + b for a, b in product(list_a, list_b)]

list_3: list[str] = concatenate_list(list_1, list_2)

print(f"Result: {list_3}")