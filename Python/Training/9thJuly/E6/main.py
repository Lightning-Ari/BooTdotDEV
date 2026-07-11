"""
Exercise 6. Count Even and Odd Numbers
Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

Exercise Purpose: This introduces Flow Control and the Modulo Operator. 
It is a classic “Filtering” pattern where you categorize data based on a mathematical property. 
In real-world apps, this is the foundation for things like alternating row colors in a table or batching jobs into two different queues.

Given Input: Numbers: [10, 21, 4, 45, 66, 93, 11]
"""

new_list: list[int] = [10, 21, 4, 45, 66, 93, 11]

even_count: int = 0
odd_count: int = 0

for num in new_list:
    if num%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"The even count is {even_count} and odd count is {odd_count} from the list {new_list}")

