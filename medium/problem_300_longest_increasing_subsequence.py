"""This file contains my solutions to Leetcode problem 300: Longest Increasing Subsequence."""



# time complexity: O(n^ 2), where 'n' is the length of nums
# space complexity: O(n)
class Solution:
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        memo = [None] * len(nums)
        for i in range(len(nums)):
            longest = max(
                longest,
                self.longest_increasing_subsequence(nums, i, memo)
            )
        return longest
    
    def longest_increasing_subsequence(self, nums, i, memo):
        if memo[i] is not None:
            return memo[i]
        longest = 1
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                longest = max(
                    longest,
                    self.longest_increasing_subsequence(nums, j, memo) + 1
                )
        memo[i] = longest
        return longest


# Bottom up with Memoization going backwards
# time complexity: O(n^ 2), where 'n' is the length of nums
# space complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = [1] * len(nums)
        longest_increasing_subsequence = 1
        for i in range(len(nums) - 2, - 1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    memo[i] = max(memo[i], 1 + memo[j])
                    longest_increasing_subsequence = max(
                        longest_increasing_subsequence,
                        memo[i]
                    )
                   
        return longest_increasing_subsequence


# Bottom up with Memoization going forwardss
# time complexity: O(n^ 2), where 'n' is the length of nums
# space complexity: O(n)
class Solution:
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        memo = [1] * len(nums)
        for end in range(1, len(nums)):
            for start in range(end):
                if nums[end] > nums[start]:
                    memo[end] = max(
                        memo[end],
                        memo[start] + 1
                    )
                    longest = max(
                        longest,
                        memo[end]
                    )
        return longest