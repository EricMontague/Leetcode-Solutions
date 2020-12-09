"""This file contains my solution to Leetcode problem 1679."""


# One Pass solution
# time complexity: O(n), where 'n' is the length of nums
# space complexity: O(n)
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        max_operations = 0
        num_counts = defaultdict(int)
        for num in nums:
            difference = target - num
            if difference in num_counts and num_counts[difference] > 0:
                num_counts[difference] -= 1
                max_operations += 1
            else:
                num_counts[num] += 1
        return max_operations


# Two pass solution
# time complexity: O(n), where 'n' is the length of nums
# space complexity: O(n)
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 1:
            return 0
        num_counts = self.build_num_counts(nums)
        max_operations = 0
        for num in nums:
            difference = target - num
            if (
                difference in num_counts 
                and num_counts[difference] > 0 
                and num_counts[num] > 0
            ):
                if num != difference:
                    max_operations += 1
                    num_counts[difference] -= 1
                    num_counts[num] -= 1
                else:
                    if num_counts[difference] >= 2:
                        max_operations += 1
                        num_counts[difference] -= 2
        return max_operations
    
    def build_num_counts(self, nums):
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1
        return num_counts

# Sorting solution
# time complexity: O(nlogn), where 'n' is the length og nums
# space complexity: Depends on sorting algorithm used
class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        max_operations = 0
        if not nums:
            return max_operations
        nums.sort()
        start = 0
        end = len(nums) - 1
        while start < end:
            sum_ = nums[start] + nums[end]
            if sum_ == target:
                max_operations += 1
                start += 1
                end -= 1
            elif sum_ < target:
                start += 1
            else:
                end -= 1
        return max_operations