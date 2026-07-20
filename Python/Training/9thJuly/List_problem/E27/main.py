"""
Exercise 27. Find the Most Frequent Element

Practice Problem: Create a script that identifies the “Mode” of a list—the element that appears most frequently. If there is a tie, returning one of the top elements is sufficient for this exercise.

Exercise Purpose: Finding the mode is a fundamental task in data science and statistics. This exercise introduces Frequency Mapping using dictionaries, a vital pattern for counting occurrences in any programming language.

Given Input: List: [1, 3, 3, 2, 1, 1, 4, 3, 3]

Expected Output: Mode: 3
"""




original_list: list[int] = [1, 3, 3, 2, 1, 1, 4, 3, 3]
temp_list: list[int] = original_list[:]
distint_list: list[int] = list(set(temp_list))
coount_list: list[int] = []

data: int = original_list.count(3)

    #create the  count
for num in distint_list:
    coount_list.append(temp_list.count(num))

high_count: int = max(coount_list)

high_count_indx: int = coount_list.index(high_count)

result: int = distint_list[high_count_indx]


print(f"Mode : {result}")

"""
This function calculates the mode using an optimized frequency dictionary. 
Inside the for loop, I leverage the .get() method with a fallback default of zero. 
This allows me to safely increment the tally for existing items and initialize new items in a single, clean line of code, 
completely eliminating the need for an explicit if/else block.

Once the frequency map is built in linear time, I pass the dictionary to the max() function using key=frequency.get. 
This evaluates the hidden count scores and directly returns the element that appeared the most frequently."
"""

def find_mode(arr: list[int])-> int :
    frequency: dict[int, int] = {}
    
    # Count occurrences of each element
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Find the key with the maximum value
    mode: int = int(max(frequency, key=frequency.get))
    return mode

# Test the function
List_test: list[int] = [1, 3, 3, 2, 1, 1, 4, 3, 3]
result = find_mode(List_test)
print(f"List: {List_test}")
print(f"Mode: {result}")