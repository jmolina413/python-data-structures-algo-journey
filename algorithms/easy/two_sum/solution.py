class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers and a target value, return the indices
        of the two numbers that add up to the target.

        :param nums: List[int] - Array of integers
        :param target: int - Target sum
        :return: List[int] - Indices of the two numbers
        """
        num_dict = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num  # Find the complement that adds up to target

            # Check if the complement is already in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]  # Return indices

            # Add the current number to the dictionary
            num_dict[num] = i

        return []  # Return an empty list if no solution is found

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test Cases
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test Case 1:", solution.twoSum(nums1, target1))  # Output: [0, 1]

    nums2 = [3, 2, 4]
    target2 = 6
    print("Test Case 2:", solution.twoSum(nums2, target2))  # Output: [1, 2]

    nums3 = [3, 3]
    target3 = 6
    print("Test Case 3:", solution.twoSum(nums3, target3))  # Output: [0, 1]
