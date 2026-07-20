"""
Exercise 4. Find Maximum and Minimum from List
Practice Problem: Identify the largest and smallest numerical values within a provided list.

Exercise Purpose: Finding extremes is vital for tasks like identifying the “best” price, the “highest” score, or detecting “outlier” data points in a dataset.

Given Input: Data: [45, 12, 89, 2, 67]

"""

new_list: list[int] = [45, 12, 89, 2, 67]
print(f"Smalest number is {min(new_list)} from the list {new_list}")
print(f"Largest number is {max(new_list)} from the list {new_list}")

min_temp: int = new_list[0]
max_temp: int = new_list[0]
for i in range(len(new_list)):
    if new_list[i] <= min_temp :
        min_temp = new_list[i]
    if new_list[i] >= max_temp :
        max_temp = new_list[i]

print(f"The largest number is {max_temp} and smallest number is {min_temp} from the list {new_list}")


min_temp: int = new_list[0]
max_temp: int = new_list[0]
for num in new_list:
    if num < min_temp:
        min_temp = num
    if num > max_temp:
        max_temp = num

print(f"The largest number is {max_temp} and smallest number is {min_temp} from the list {new_list}")

