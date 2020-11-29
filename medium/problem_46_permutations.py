"""This file contains my solutions to Leetcode problem 46: Permutations."""


# time complexity: O(n * n!), where 'n' is the number of integers in the
# list
# space complexity: O(n * n!), since we need space for n! permutations
# and each permutation contains 'n' elements

# This solution recursively generates all permutations by generating
# all permutations that start with a specific integer in the list

# E.g. If the input is [2,3,7], it will first generate all permutations
# that begin with 2, then all permutations that begin with 3, and finally
# all permutations the begin 7
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        permutations = []
        permutation = []
        self.generate_permutations(nums, permutation, permutations)
        return permutations

    def generate_permutations(self, nums, permutation, permutations):
        if not nums:
            permutations.append(permutation[:])
        else:
            for index, num in enumerate(nums):
                permutation.append(num)
                self.generate_permutations(
                    nums[0:index] + nums[index + 1 :], permutation, permutations
                )
                permutation.pop()


# Alternative Solution without slicing
# time complexity: O(n * n!), where 'n' is the number of integers in the
# list
# space complexity: O(n * n!), since we need space for n! permutations
# and each permutation contains 'n' elements
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        current_permutation = []
        permutations = []
        chosen = set()
        self.generate_permutations(nums, current_permutation, permutations, chosen)
        return permutations

    def generate_permutations(self, nums, current_permutation, permutations, chosen):
        if len(current_permutation) == len(nums):
            permutations.append(current_permutation[:])
        else:
            for num in nums:
                if num not in chosen:
                    current_permutation.append(num)
                    chosen.add(num)
                    self.generate_permutations(
                        nums, current_permutation, permutations, chosen
                    )
                    current_permutation.pop()
                    chosen.remove(num)



# Iterative Solution #1

# This solution uses BFS to first generate all permutations
# from indices 0 to 0 (inclusive), then all permutations from
# indices 0 to 1 (inclusive), then all permutaions from
# indices 0 to 2 etc.

# e.g. if the input is [7,3,2], it will first start with an empty
# permutation of size 0 in the queue. Then it will create all permutations
# up until index 0 ([7]). Next it will create all permutations up until
# index 1 ([7, 3], [3, 7]). This can be thought of as creating all permutations
# that contain 7 and 3. Finally it will create all permutations that contains 7, 3,
# 2 ([7, 3, 2], [7, 2, 3], [2, 3, 7], [2, 7, 3], [3, 7, 2], [3, 2, 7]). Each step
# builds off of the permutations created in the prior step of the algorithm



# time complexity: O(n * n!), where 'n' is the number of integers in the
# list
# space complexity: O(n * n!), since we need space for n! permutations
# and each permutation contains 'n' elements
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = deque([[]])
        for current_number in nums:
            size = len(permutations)
            for i in range(size):
                old_permutation = permutations.popleft()
                for j in range(len(old_permutation) + 1):
                    new_permutation = old_permutation.copy()
                    new_permutation.insert(j, current_number)
                    if len(new_permutation) == len(nums):
                        result.append(new_permutation)
                    else:
                        permutations.append(new_permutation)
        return result