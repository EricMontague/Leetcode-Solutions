"""This is my solution to Leetcode Problem: 42, Trapping Rain Water."""


# time complexity: O(n), where 'n' is the number of integers in heights
# space complexity: O(n), where 'n' is the number of integers in heights
class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        maxLeftHeights = self.findMaxLeftHeights(heights)
        return self.findRainwater(heights, maxLeftHeights)
       
    def findMaxLeftHeights(self, heights):
        maxLeftHeights = [0] * len(heights)
        for index in range(len(heights)):
            if index == 0:
                maxLeftHeights[index] = heights[index]
            else:
                maxLeftHeights[index] = max(heights[index], maxLeftHeights[index - 1])
        return maxLeftHeights

    def findRainwater(self, heights, maxLeftHeights):
        maxRightHeight = heights[len(heights) - 1]
        rainwater = 0
        for index in range(len(heights) - 2, -1, -1):
            maxRightHeight = max(heights[index], maxRightHeight)
            minHeight = min(maxLeftHeights[index], maxRightHeight)
            rainwater += (minHeight - heights[index])
        return rainwater
        
        