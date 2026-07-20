"""
Exercise 15. Find the Longest String in a List
Practice Problem: In a list of strings, identify which string has the most characters.

Exercise Purpose: This combines Iteration with Comparison. It teaches you how to evaluate an attribute of an object (its length) rather than just its raw value. This is used in text processing, UI layout, and data cleaning.

Given Input: Words: ["PHP", "Exercises", "Backend", "Python"]

Expected Output: Longest word: Exercises
"""
words: list[str] = ["PHP", "Exercises", "Backend", "Python"]
character_count: int = 0
result: str = words[0]

for word in words:
    if len(word) > character_count:
        character_count = len(word)
        result = word

print(f"Longest word: {result}")


words: list[str] = ["PHP", "Exercises", "Backend", "Python"]

# Find the maximum item based on the len function
result: str = max(words, key=len)

print(f"Longest word: {result}")
# Output: Longest word: Exercises


# Find the mainimum item based on the len function
result: str = min(words, key=len)

print(f"Smalest word: {result}")
# Output: Longest word: Exercises