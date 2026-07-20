"""
Exercise 28. Extract Every Nth Element from a List

Practice Problem: Write a function that accepts a list and an integer n, 
returning a new list containing every nth element from the original, starting from the first element (index 0).

Exercise Purpose: This exercise explores List Slicing, one of Python’s most powerful features. 
Understanding slicing notation allows you to manipulate sequences with minimal code, which is essential for tasks like data sampling.

Given Input:

    List: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    n: 3

Expected Output: Result: ['a', 'd', 'g']
"""

def nth_element(numbres: list[str], pos: int) -> list[str]:
    # Start at 0, go to the end, step by 'pos'
    return numbres[::pos]

number_list: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
nth_num: int = 3

result: list[str] = nth_element(number_list, nth_num)
print(f"Result : {result}")
# Output: Result : ['a', 'd', 'g']



"""
1. The Core Explanation (The "What")
"In Python, the most efficient way to extract every Nth element is using slice notation with a stride, 
written as list[start:stop:step]. By omitting the start and stop boundaries and setting the step to N (list[::N]), 
Python defaults the starting point to index 0. It immediately captures the first element, and then increments the index by N 
for each subsequent element."

2. The Step-by-Step Walkthrough (The "How")
"For a list like ['a', 'b', 'c', 'd', 'e', 'f', 'g'] with a step of 3:
    It starts at index 0, so it grabs 'a' immediately.
    It then strides 3 steps forward to index 3, which grabs 'd'.
    It strides 3 more steps forward to index 6, which grabs 'g'.
    This perfectly satisfies the requirement of starting from the first element."

3. The Engineering Justification (The "Why")
"I prefer this over a manual for loop with an index counter for three reasons:
    
    Performance: Slicing is implemented internally in C. 
    It runs much faster than iterating and appending elements in a Python loop.
    
    Readability: It is the industry standard 'Pythonic' way to sample sequences, 
    making the code instantly understandable to other Python engineers.
    
    Maintainability: It eliminates the boilerplate code of managing state counters, 
    which drastically reduces the surface area for logic bugs."
"""

