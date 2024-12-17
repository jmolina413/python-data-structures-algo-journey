# Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`.

### Example
**Input**: `nums = [2, 7, 11, 15]`, `target = 9`  
**Output**: `[0, 1]`  

### Approach
1. Use a **hash map (dictionary)** to store the number and its index as we iterate through the array.  
2. For each number, check if `target - num` exists in the dictionary.  
3. If it exists, return the indices.  

### Python Code
```python
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []