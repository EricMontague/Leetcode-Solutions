"""This file contains my solutions to Leetcode problem 78: Subsets."""


# time complexity: O(n * 2^n), where 'n' is the length os nums
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_subsets = [[]]
        
        for num in nums:
            new_subsets = []
            for subset in final_subsets:
                new_subsets.append([num] + subset)
            for new_subset in new_subsets:
                final_subsets.append(new_subset)
        return final_subsets


# time complexity: O(n * 2^n), where 'n' is the length os nums
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.build_subsets(nums, len(nums) - 1, [], subsets)
        return subsets
    
    def build_subsets(self, nums, index, subset, subsets):
        if index == -1:
            subsets.append(subset)
        else:
            left_subset = subset + [nums[index]]
            right_subset = subset[:]
            self.build_subsets(nums, index - 1, left_subset, subsets)
            self.build_subsets(nums, index - 1, right_subset, subsets)
            