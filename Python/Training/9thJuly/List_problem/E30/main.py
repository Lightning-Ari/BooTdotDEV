"""
Exercise 30. Find All Common Elements Between Three Lists

Practice Problem: Given three separate lists, 
write a function that returns a list containing only the elements that appear in all three.

Exercise Purpose: This exercise introduces Set Intersection. 
When you need to find commonalities across multiple data sources, 
converting them to sets and finding their intersection is the most efficient method (O(n) average time complexity).

Given Input:

    List A: [1, 5, 10, 20]
    List B: [6, 7, 20, 80, 100]
    List C: [3, 4, 15, 20, 30, 70, 80]

Expected Output: Common Elements: [20]
"""

def common_element(list1: list[int], list2: list[int], list3: list[int]) -> list[int]:
    # Convert lists to sets and find where they overlap (intersection)
    common_set = set(list1) & set(list2) & set(list3)
    
    # Convert the result back to a list
    return list(common_set)

list_a: list[int] = [1, 5, 10, 20]
list_b: list[int] = [6, 7, 20, 80, 100]
list_c: list[int] = [3, 4, 15, 20, 30, 70, 80]

result: list[int] = common_element(list_a, list_b, list_c)

print(f"Common Elements: {result}")

"""
Step 1: Explain Your Initial Thought (The Brute-Force Approach)
    "To solve this, my initial instinct was a brute-force approach using nested loops. I iterated through list1, nested a loop for list2, and nested a third loop for list3 to find where the elements matched. While this logic is perfectly correct and easy to read, it has a major drawback: it runs in \(O(N^3)\) time complexity. If the input lists grew large, this nested loop approach would cause a massive performance bottleneck."

Step 2: Introduce the Optimized Solution (The Set Intersection)
    "To optimize this for production and achieve \(O(N)\) linear time complexity, I would leverage Python's built-in set data structure. Sets use hashing, which allows for \(O(1)\) constant-time lookups. By converting the lists into sets, I can use the set intersection operator (&) to instantly grab the common elements across all three datasets."
Step 3: Write out the Code  


"""