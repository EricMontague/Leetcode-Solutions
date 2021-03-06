"""This file contains my solutions to Leetcode problem 78: Subsets."""


# Iterative solution

# This solution works by building the subsets incrementally
# First you create all possible subsets that can be created from
# just the first element in the list. Then, you create all subsets
# than can be created from the first 2 elements in the list.
# Then you create all subsets that can be created from the first 3
# elements and so on an so forth.


# The major insight is that all subsets that contain the first
# 2 elements can be created by adding the 2nd element to all
# subsets that contain 0 and 1 element. Then, all subsets that
# contain the first 3 elements can be created by adding the 3rd element
# to all subsets that contain 0, 1, and 2 elements. This pattern
# repeats until you have generated all possible UNIQUE subsets

# See visual explanation: https://leetcode.com/problems/subsets/Figures/78/recursion.png


# time complexity: O(n * 2^n), where 'n' is the length os nums
# space complexity: O(n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for current_number in nums:
            new_subsets = []
            for previous_subset in subsets:
                new_subsets.append(previous_subset + [current_number])
            for new_subset in new_subsets:
                subsets.append(new_subset)
        return subsets
        

# Recursive Version of the above solution
# time complexity: O(n * 2^n), where 'n' is the length os nums
# space complexity: O(n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.generate_subsets(nums, len(nums) - 1)
    
    def generate_subsets(self, nums, index):
        if index == -1:
            return [[]]
        previous_subsets = self.generate_subsets(nums, index - 1)
        new_subsets = []
        for subset in previous_subsets:
            new_subsets.append(subset + [nums[index]])
        previous_subsets.extend(new_subsets)
        return previous_subsets


    
# Backtracking solution
# The idea of this solution is to first generate all subsets
# of length 0, then generate all subsets of length 1, then all
# subsets of length 2, and so on all the way to subsets of length n.


# time complexity: O(n * 2^n), where 'n' is the length os nums
# space complexity: O(n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for subset_size in range(len(nums) + 1):
            self.generate_subsets(nums, subsets, [], subset_size, 0)
        return subsets
    
    def generate_subsets(self, nums, subsets, current_subset, size, start):
        if size == 0:
            subsets.append(current_subset[:])
        else:
            for end in range(start, len(nums)):
                current_subset.append(nums[end])
                self.generate_subsets(
                    nums,
                    subsets,
                    current_subset,
                    size - 1,
                    end + 1
                )
                current_subset.pop()


# Another Backtracking solution
# This solution models out the idea that for each element in
# the set, you can either include it in the subset, or you choose
# not to include it in the subset. Each recursive call models 
# the possible subsets you can generate had you decided to include or
# not include a particular element in a subset


# time complexity: O(n * 2^n), where 'n' is the length os nums
# space complexity: O(n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current_subset = []
        start_index = 0
        self.generate_subsets(
            nums, 
            start_index,
            current_subset,
            subsets
        )
        return subsets
    
    def generate_subsets(self, nums, index, current_subset, subsets):
        if index >= len(nums):
            subsets.append(current_subset.copy())
        else:
            current_subset.append(nums[index])
            self.generate_subsets(
                nums,
                index + 1,
                current_subset,
                subsets
            )
            current_subset.pop()
            self.generate_subsets(
                nums,
                index + 1,
                current_subset,
                subsets
            )