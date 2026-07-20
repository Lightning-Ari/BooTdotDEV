"""
Exercise 29. Check if List is Palindrome

Practice Problem: Determine if a list reads the same forward and backward. 
The function should return True if it is a palindrome and False otherwise.

Exercise Purpose: Palindrome checks are classic logic tests. 
This exercise demonstrates how to compare a sequence against its own reverse, 
reinforcing concepts of Symmetry and sequence comparison.

Given Input: List: [1, 2, 3, 2, 1]

Expected Output: Is Palindrome: True
"""

def is_palindrome(lst: list[int]) -> bool:
    # Compare the list to its reverse
    return lst == lst[::-1]

# Test cases
test1 = [1, 2, 3, 2, 1]
test2 = [1, 2, 3, 4, 5]

print(f"{test1} is palindrome? {is_palindrome(test1)}")
print(f"{test2} is palindrome? {is_palindrome(test2)}")