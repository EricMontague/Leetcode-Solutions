"""This file contains my solutions for Leetcode problem 55: Jump Game."""


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:    
        if not nums:
            return False
        last_position = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0


# time complexity: O(n ^ 2)
# space complexity: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        memo = [None] * len(nums)
        return self.can_reach_end(nums, 0, memo)
    
    def can_reach_end(self, nums, index, memo):
        if memo[index] is not None:
            return memo[index]
        if index == len(nums) - 1:
            memo[index] = True
            return True
        for jump in range(1, min(nums[index], len(nums) - index - 1) + 1):
            if self.can_reach_end(nums, index + jump, memo):
                memo[index] = True
                return True
        memo[index] = False
        return False



# time complexity: O(n ^ 2)
# space complexity: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:    
        if not nums:
                return False
            memo = [None] * len(nums)
            memo[-1] = True
            for i in range(len(nums) - 2, -1, -1):
                for j in range(1, min(nums[i], len(nums) - i - 1) + 1):
                    if memo[i + j]:
                        memo[i] = True
                        break
            return memo[0]