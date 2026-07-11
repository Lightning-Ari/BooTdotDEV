"""
Exercise 3. Sum and Average of All Numbers in a List
Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).

Exercise Purpose: Aggregation is the heart of data science. This exercise teaches you how to reduce a collection of multiple data points into a single, meaningful summary statistic.

Given Input: Numbers: [10, 20, 30, 40, 50]
"""

new_list = [10, 20, 30, 40, 50]

print(f"The sum of the list is {sum(new_list)} and the average of the list is {sum(new_list)/len(new_list)} from the list {new_list}")

sum_total: int = 0
count: int = 0
for num in new_list:
    sum_total += num
    count += 1
average: float = sum_total / count

print(f"sum of the list {sum_total} and average of the list {average} from the list {new_list}")




