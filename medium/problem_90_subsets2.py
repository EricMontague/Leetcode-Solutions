"""This file contains my solutions to Leetcode problem 90: Subsets II."""


# time complexity: O(N* 2^N), where 'N' is the length of nums
# space complexity: O(N* 2^N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        for num_index in range(len(nums)):
            new_subsets = []
            start_index = 0
            if num_index > 0 and nums[num_index] == nums[num_index - 1]:
                start_index = end_index + 1
            end_index = len(subsets) - 1
            for subset_index in range(start_index, end_index + 1):
                new_subsets.append(subsets[subset_index] + [nums[num_index]])
            subsets.extend(new_subsets)
        return subsets




# Backtracking solution

# The idea here is to first sort the input so that duplicates are
# next to each other. Then you use recursion and backtracking
# to generate the subsets. What you notice is that if the prior value
# in the window (subarray) of the array you're currently in is equal to the current 
# value you're at, then you will end up creating a duplicate subset. So, 
# to handle this, you skip recursing in this instance.


# time complexity: O(N* 2^N), where 'N' is the length of nums
# space complexity: O(N* 2^N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        for subset_size in range(len(nums) + 1):
            self.generate_subsets(nums, subset_size, 0, [], subsets)
        return subsets
    
    def generate_subsets(self, nums, size, start, current_subset, subsets):
        if size == 0:
            subsets.append(current_subset.copy())
        else:
            for end in range(start, len(nums)):
                if end > 0 and end - 1 >= start and nums[end] == nums[end - 1]:
                    continue
                current_subset.append(nums[end])
                self.generate_subsets(
                    nums,
                    size - 1,
                    end + 1,
                    current_subset,
                    subsets
                )
                current_subset.pop()


# Same solution as above with slicing. More understandle since there is
# no need to keep track of what subarray of the array you are in
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        for subset_size in range(len(nums) + 1):
            self.generate_subsets(nums, subset_size, [], subsets)
        return subsets
    
    def generate_subsets(self, nums, size, current_subset, subsets):
        if size == 0:
            subsets.append(current_subset.copy())
        else:
            for j in range(len(nums)):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                current_subset.append(nums[j])
                self.generate_subsets(
                    nums[j + 1:],
                    size - 1,
                    current_subset,
                    subsets
                )
                current_subset.pop()