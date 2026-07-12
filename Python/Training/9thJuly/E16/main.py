"""
Exercise 16. Turn Every Item of a List into its Square (List Comprehension)
Practice Problem: Given a list of numbers, create a new list where each number is replaced by its square (n2) using a single line of code.

Exercise Purpose: This is your introduction to List Comprehensions. 
In Python, writing a full for loop to build a new list is often considered un-Pythonic. 
List comprehensions execute faster and are cleaner to read, providing a concise way to map a function across a collection.

Given Input: List: [1, 2, 3, 4, 5]

Expected Output: Squared List: [1, 4, 9, 16, 25]
"""

number_list: list[int] = [1, 2, 3, 4, 5]
squared_list: list[int] = [value** 2 for value in number_list]
print(f"Squared List: {squared_list}")


