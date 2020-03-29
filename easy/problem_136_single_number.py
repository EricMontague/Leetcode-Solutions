"""This script contains my solution to problem 136."""

from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num in nums:
            if counts[num] == 1:
                return num

#Overall time complexity: O(n)
#Overall space complexity: O(n)
