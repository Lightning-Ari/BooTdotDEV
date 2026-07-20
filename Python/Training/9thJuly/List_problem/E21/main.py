"""
Exercise 21. List Comprehension for Filtering Numbers

Practice Problem: Given a list of integers, 
use list comprehension to create a new list that contains only the even numbers from the original list.

Exercise Purpose: This is the “Filter” part of the Map-Filter-Reduce paradigm.
Here we focuses on Conditional Logic within a single line. 
It is the gold standard for creating subsets of data based on specific criteria.

Given Input: List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Expected Output: Even Numbers: [2, 4, 6, 8, 10]
"""

original_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list: list[int] = [num for num in original_list if num %2 == 0]

print(f"Even Numbers: {new_list}")

#leverage boolean evaluation

"""
In Python, num % 2 returns 1 for odd numbers (which means True) and 0 for even numbers (which means False).
Therefore, not num % 2 becomes True only for even numbers.
"""

new_list: list[int] = [num for num in original_list if not num %2]
print(f"Even Numbers: {new_list}")


"""
"According to the exercise requirements, I used a list comprehension to filter the dataset.
 First, I initialized original_list containing integers from 1 to 10.
 Next, I created new_list using square brackets to house the comprehension. Inside it,
   I set up a for loop to iterate through each item in the original list. For every item,
   Python evaluates the conditional statement at the end: if num % 2 == 0. 
   This uses the modulo operator to check if the number is perfectly divisible by two with a remainder of zero.
   If the condition is met, the variable num at the front is passed into the new list. Finally, 
   the formatted print function outputs the clean array of even numbers."
"""