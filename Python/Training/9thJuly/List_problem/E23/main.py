"""
Exercise 23. Iterate Both Lists Simultaneously

Practice Problem: Use the zip() function to loop through two lists at once and print their values as pairs.

Exercise Purpose: Iterating through two lists with a single index variable is error-prone 
(you might hit an “Index Out of Range” if lists are different sizes). zip() is the Safe Parallel Iterator. 
It stops automatically at the end of the shortest list, preventing crashes.

Given Input:

    List 1: [10, 20, 30]
    List 2: [100, 200, 300]
Output:
    10 100
    20 200
    30 300
"""

list_one: list[int] = [10, 20, 30]
list_two: list[int] = [100, 200, 300]

for a, b in zip(list_one, list_two):
    print(f"{a} {b}")


"""
An Interviewer's Twist: What if the lists are uneven?
    Since you already know how zip() works, 
    an interviewer will often throw a curveball to see how deeply you understand it. 
    They might ask: "What if list_two had a fourth element, like 400, 
    but you still wanted to print it?"By default, zip() drops that extra data. 
    To handle uneven lists without dropping data, you can introduce a built-in module tool called zip_longest:

    
"""

from itertools import zip_longest

list_one: list[int] = [10, 20, 30]
list_two: list[int] = [100, 200, 300, 400]  # Uneven list

# zip_longest keeps going and fills missing values with a placeholder (None by default)
for a, b in zip_longest(list_one, list_two, fillvalue="-"):
    print(f"{a} {b}")

# Output:
# 10 100
# 20 200
# 30 300
# - 400
