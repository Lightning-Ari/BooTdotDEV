"""
Exercise 8. Sort a List of Numbers
Practice Problem: Sort a list of numbers in ascending order (lowest to highest).

Exercise Purpose: Sorting is perhaps the most studied topic in Computer Science. It turns chaotic data into organized data, which is a prerequisite for high-speed search algorithms like Binary Search. Python uses Timsort, an efficient, hybrid sorting algorithm.

Given Input: Unsorted: [56, 12, 89, 3, 22]

Expected Output: Sorted List: [3, 12, 22, 56, 89] 
"""

new_list: list[int] = [56, 12, 89, 3, 22]
second_list: list [int] = new_list[:]
print(f"Tempurary Sorted list {sorted(new_list)} from {new_list}")
new_list.sort()
print(f"permanent Sorted list {new_list}")

print(f"Tempurary Sorted Second list in decending order {sorted(second_list, reverse = True)} from {second_list}")
second_list.sort(reverse= True)
print(f"permanent Sorted list {second_list}")