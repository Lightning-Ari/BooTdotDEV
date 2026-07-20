"""
Exercise 22. Concatenate Two Lists Index-wise

Practice Problem: Given two lists of strings, combine them index-by-index to form a single list of concatenated strings.

Exercise Purpose: Data is often stored in parallel lists (e.g., First Names and Last Names). 
This exercise teaches you how to merge parallel data into a usable format, a common need for report generation and UI display.

Given Input:

    List 1: ["Py", "is", "awes"]
    List 2: ["thon", " ", "ome"]

Expected Output: Merged: ['Python', 'is ', 'awesome']
"""

list_one: list[str] = ["Py", "is", "awes"]
list_two: list[str] = ["thon", " ", "ome"]

# Zip pairs 'Py' with 'thon', 'is' with ' ', etc.

merged_list: list[str] = [a + b for a, b in zip(list_one, list_two)]

print(f"Merged: {merged_list}")

"""
1. The High-Level Summary (The What)
    "This script combines two parallel arrays of string fragments index-by-index. 
    To achieve this cleanly, I used a list comprehension combined with Python's built-in zip() 
    function to merge the string segments into a single, unified list."

2. The Line-by-Line Breakdown (The How)
    "First, we initialize list_one and list_two containing our string components.
    
    Next, we declare merged_list. Inside the square brackets, 
    Python evaluates the right side first: zip(list_one, list_two). 
    The zip function acts as a generator that pairs up the elements from both arrays side-by-side based on their index positions.

    We then unpack each pair into two temporary variables, 
    a and b, using a for loop. For each iteration, the expression a + b concatenates the two strings together.
    These newly formed strings are automatically collected and returned in our final list."

3. Proving Your Expertise (The Why)
    "I deliberately chose zip() over a traditional range(len()) loop for two major reasons:

    First, it prevents IndexError crashes. 
    If one list accidentally becomes shorter than the other, zip() will safely stop iterating at the shortest list, 
    whereas a manual index loop would crash the program.

    Second, it makes the code highly readable and Pythonic by eliminating noisy bracket notation like list_one[i],
     and it executes at optimized C-speed under the hood."
"""