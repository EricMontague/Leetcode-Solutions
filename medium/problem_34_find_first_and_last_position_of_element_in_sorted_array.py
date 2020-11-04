"""This file contains my solutions to Leetcode problem 34:
Find First and Last Position of Element in Sorted Array.

"""


# Binary Search Solution Recursive
# time comeplxity: O(log n), where 'n' is the length of nums
# space complexity: O(log n)
class Solution:
    
    FIRST = 0
    LAST = 1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        positions = [-1, -1]
        first_position = self.find_position(nums, 0, len(nums), target, self.FIRST)
        if first_position == len(nums) or nums[first_position] != target:
            return positions
        last_position = self.find_position(nums, 0, len(nums), target, self.LAST)
        positions[0] = first_position
        positions[1] = last_position - 1
        return positions
    
    def find_position(self, nums, low, high, target, position):
        if low == high:
            return low
        mid = low + (high - low) // 2
        if nums[mid] > target or nums[mid] == target and position == self.FIRST:
            return self.find_position(nums, low, mid, target, position)
        return self.find_position(nums, mid + 1, high, target, position)
            


# Binary Search Solution Iterative
# time comeplxity: O(log n), where 'n' is the length of nums
# space complexity: O(1)
class Solution:
    
    FIRST = 0
    LAST = 1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        positions = [-1, -1]
        if not nums:
            return positions
        first_position = self.find_position(nums, target, self.FIRST)
        if first_position == -1:
            return positions
        last_position = self.find_position(nums, target, self.LAST)
        positions[0] = first_position
        positions[1] = last_position
        return positions
    
    def find_position(self, nums, target, position):
        low = 0
        high = len(nums) - 1
        index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                index = mid
            if target < nums[mid] or target == nums[mid] and position == self.FIRST:
                high = mid - 1
            else:
                low = mid + 1
        return index



# Naive Linear Search
# time comeplxity: O(log n), where 'n' is the length of nums
# space complexity: O(1)
class Solution2:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        positions = [-1, -1]
        found_first = False
        for index, num in enumerate(nums):
            if num == target:
                if not found_first:
                    positions[0] = index
                    positions[1] = index
                    found_first = True
                else:
                    positions[1] = index
        return positions