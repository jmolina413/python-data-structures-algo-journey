# Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to the `target`.

You may not use the same element twice, and exactly one solution exists.

---

## Example 1:
**Input**: `nums = [2, 7, 11, 15]`, `target = 9`  
**Output**: `[0, 1]`  
**Explanation**: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

## Example 2:
**Input**: `nums = [3, 2, 4]`, `target = 6`  
**Output**: `[1, 2]`  

---

## Approach
1. Use a **hash map (dictionary)** to store the numbers as keys and their indices as values.  
2. For each number in the array:
   - Calculate its complement: `complement = target - num`.
   - If the complement exists in the dictionary, return the indices.
3. Otherwise, store the current number and its index in the dictionary.

---

## Complexity Analysis
- **Time Complexity**: O(n) - We iterate through the array once, and dictionary operations are O(1).  
- **Space Complexity**: O(n) - In the worst case, we store all `n` elements in the dictionary.

---

## Python Solution
```python
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
