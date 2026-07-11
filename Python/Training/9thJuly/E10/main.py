"""
Exercise 10. Combine Two Lists
Practice Problem: Merge two separate lists into a single, unified list.

Exercise Purpose: Data often arrives in fragments from different sources (e.g., two different database queries). Combining or “Concatenating” them is the first step in data aggregation.

Given Input:

List A: ["Physics", "Chemistry"]
List B: ["Maths", "Biology"]
Expected Output: Combined List: ['Physics', 'Chemistry', 'Maths', 'Biology']
"""
list_a: list[str] = ["Physics", "Chemistry"]
list_b: list[str] = ["Maths", "Biology"]

combine_list: list[str] = list_a + list_b
list_a.extend(list_b)
"""for item in list_b:
    list_a.append(item)"""

print(f"The combine list is {list_a}")

