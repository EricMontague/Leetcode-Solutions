"""This file contains my solution to Leetcode problem 153: Find Minimum
in Rotated Sorted Array.
"""

# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return float("-inf")
        if nums[0] <= nums[-1]:
            return nums[0]
        return self.binarySearch(nums, 0, len(nums) - 1)
    
    def binarySearch(self, nums, start, end):
        mid = end + (start - end) // 2
        # greatest
        if nums[mid + 1] < nums[mid]:
            return nums[mid + 1]
        # smallest
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[start] > nums[mid]:
            return self.binarySearch(nums, start, mid - 1)
        elif nums[end] < nums[mid]:
            return self.binarySearch(nums, mid + 1, end)
