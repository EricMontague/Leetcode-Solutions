"""This file contains my solution to problem 33: Search In Rotated Sorted Array."""


# Time complexity: O(log n)
# Space Complexity: O(log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums) - 1)
    
    def binarySearch(self, nums, target, start, end):
        if start > end:
            return -1
        mid = end + (start - end) // 2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if target >= nums[start] and target < nums[mid]:
                return self.binarySearch(nums, target, start, mid - 1)
            return self.binarySearch(nums, target, mid + 1, end)
        else:
            if target <= nums[end] and target > nums[mid]:
                return self.binarySearch(nums, target, mid + 1, end)
            return self.binarySearch(nums, target, start, mid - 1)

