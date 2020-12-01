"""This file contains my solutions to Leetcode problrm 47: Permutations II."""

# Backtracking solution

# time complexity: O(n * n!), where 'n' is the number of integers in the
# list
# space complexity: O(n * n!), since we need space for n! permutations
# and each permutation contains 'n' elements
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        current_permutation = []
        permutations = []
        counter = Counter(nums)
        self.generate_permutations(
            counter, current_permutation, permutations, len(nums)
        )
        return permutations
    
    def generate_permutations(
        self, counter, current_permutation, permutations, num_integers
    ):
        if len(current_permutation) == num_integers:
            permutations.append(current_permutation.copy())
        else:
            for num in counter:
                if counter[num] > 0:
                    current_permutation.append(num)
                    counter[num] -= 1
                    self.generate_permutations(
                        counter,
                        current_permutation,
                        permutations,
                        num_integers
                    )
                    current_permutation.pop()
                    counter[num] += 1


# Iterative Solution
# time complexity: O(n * n!), where 'n' is the number of integers in the
# list
# space complexity: O(n * n!), since we need space for n! permutations
# and each permutation contains 'n' elements
from collections import deque

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        permutations = deque([[]])
        for current_number in nums:
            size = len(permutations)
            for i in range(size):
                old_permutation = permutations.popleft()
                for j in range(len(old_permutation) + 1):
                    new_permutation = old_permutation.copy()
                    new_permutation.insert(j, current_number)
                    if len(new_permutation) == len(nums):
                        results.append(new_permutation)
                    else:
                        permutations.append(new_permutation)
                    if j < len(new_permutation) - 1 and new_permutation[j + 1] == current_number:
                        break
        return results