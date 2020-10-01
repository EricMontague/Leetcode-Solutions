"""This file contains my solutions to Leetcode problem 896: Monotonic Array."""

# time complexity: O(n), where 'n' is the number of elements in the array
# space complexity: O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = False
        isDecreasing = False
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                isIncreasing = True
            elif nums[index] < nums[index - 1]:
                isDecreasing = True
            if isIncreasing and isDecreasing:
                return False
        return True
                
        