"""
Exercise 17. Count Occurrences of an Item

Practice Problem: Find out how many times a specific value appears in a list.

Exercise Purpose: This is a basic form of Frequency Analysis. It’s used in everything from counting word occurrences in a document to verifying how many times a specific error code appears in a server log.

Given Input:

    List: [10, 20, 30, 10, 40, 10, 50]
    Target: 10

Expected Output: The number 10 appears 3 times.
"""

new_list: list[int] = [10, 20, 30, 10, 40, 10, 50]
target: int = 10
count: int = new_list.count(target)



print(f" {count}")
