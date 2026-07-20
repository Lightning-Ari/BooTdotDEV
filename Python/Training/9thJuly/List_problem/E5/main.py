"""
Exercise 5. Calculate the Product of All Elements
Practice Problem: Multiply every number in a list together to find the total product.

Exercise Purpose: While sum is built-in, “product” often requires you to think about how to accumulate values. This exercise reinforces the concept of an “accumulator variable” in a loop.

Given Input: Factors: [2, 3, 5, 7]

Expected Output: Product: 210
"""

new_list: list[int] = [2, 3, 5, 7]
product: int = 1
for num in new_list:
    product *= num

print(f"The product is {product} from the list {new_list}")