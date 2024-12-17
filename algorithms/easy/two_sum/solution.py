def two_sums(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i
    return []

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", nums, "Target:", target)
    print("Output Indices:", two_sums(nums, target))  # Output: [0, 1]