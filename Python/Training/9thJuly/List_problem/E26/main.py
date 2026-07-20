"""
Exercise 26. Find the Second Largest Number in a List

Practice Problem: Write a Python function that takes a list of numbers and returns the second largest value. 
Ensure the function handles lists with duplicate values correctly (e.g., if the list is [10, 10, 9], the second largest is 9).

Exercise Purpose: This exercise teaches you how to process data sets where “rank” matters. 
It also highlights the importance of handling duplicates. Simply sorting a list does not work 
if the largest number appears multiple times. It introduces the concept of using Sets to make data unique.

Given Input: List: [12, 35, 1, 10, 34, 1, 35]

Expected Output: Second Largest: 34
"""

def second_number(numbes: list[int]) -> int:
    result: int = 0
    
    #remove duplicate of the list
    new_list: list[int] = list(set(numbes))

    # check the length of the list
    if len(new_list) < 2:
        raise Exception("List length is less than 2 items.")
    
    

    #sort the list
    new_list.sort(reverse= True)

    #find second value
    result = new_list[1]

    return result


original_list: list[int] = [12, 35, 1, 10, 34, 1, 35]

#removing duplicate
updated_list: list[int] = list(dict.fromkeys(original_list))

#sort operation on updated list
updated_list = sorted(updated_list, reverse= True)

#find the second largest number on the list
second_num: int = updated_list[1]

#testing
print(f"{updated_list}")

#output

print(f"Second Largest: {second_num}")


#2nd try
temp_list: list[int] = original_list[:]


print(f"Second Largest: {second_number(original_list)}")