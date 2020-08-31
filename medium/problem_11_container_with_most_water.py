"""This file contains my solution to Leetcode problem 11: Container with Most Water."""

# time complexity: O(n), where 'n' is the number of elements in heights
# space complexity: O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = float("-inf")
        low = 0
        high = len(heights) - 1
        while low < high:
            height = min(heights[low], heights[high])
            width = high - low
            maxArea = max(maxArea, height * width)
            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1
        return maxArea