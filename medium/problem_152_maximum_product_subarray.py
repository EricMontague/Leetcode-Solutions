"""This file contains my solution to Leetcode problem 152."""


# Time complexity: O(n), where "n" is the number of integers in nums
# Space complexity: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float("-inf")
        currentMaxProduct = 1
        currentMinProduct = 1
        for num in nums:
            newCurrentMax = max(num, num * currentMaxProduct, num * currentMinProduct)
            newCurrentMin = min(num, num * currentMaxProduct, num * currentMinProduct)
            currentMaxProduct = newCurrentMax
            currentMinProduct = newCurrentMin
            maxProduct = max(currentMaxProduct, maxProduct)
        return maxProduct

