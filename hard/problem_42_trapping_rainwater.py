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
        

# Recursive solution:
# time complexity: O(n), where 'n' is the total number of integers in height
# space complexity: O(n), where 'n' is the total number of integers in height
class Solution:
    rainwater = 0
    def trap(self, height: List[int]) -> int:
        if not height:
            return self.rainwater
        startingIndex = 0
        self.getElevationHeight(height, height[0], startingIndex)
        return self.rainwater
    
    def getElevationHeight(self, height, maxHeight, currentIndex):
        if currentIndex == len(height) - 1:
            return height[currentIndex]
        newMaxHeight = max(height[currentIndex], maxHeight)
        elevationHeight = self.getElevationHeight(height, newMaxHeight, currentIndex + 1)
        minHeight = min(elevationHeight, newMaxHeight)
        rainwater = minHeight - height[currentIndex]
        if rainwater <= 0:
            return height[currentIndex]
        self.rainwater += rainwater
        return height[currentIndex] + rainwater


# Stack Solution:
# time complexity: O(n), where 'n' is the number of integers in heights
# space complexity: O(n), where 'n' is the number of integers in heights
class Solution:
    def trap(self, heights: List[int]) -> int:
        totalWater = 0
        stack = []
        for index, currentHeight in enumerate(heights):
            while stack and currentHeight > heights[stack[-1]]:
                target = stack.pop()
                if stack:
                    distance = index - stack[-1] - 1
                    newTop = stack[-1]
                    boundedHeight = min(currentHeight, heights[newTop]) - heights[target]
                    totalWater += distance * boundedHeight
            stack.append(index)
        return totalWater


# Two pointer solution:
# time complexity: O(n), where 'n' is the number of integers in heights
# space complexity: O(1)
class Solution:
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        totalWater = 0
        leftMax = 0
        rightMax = 0
        while left < right:
            if heights[left] < heights[right]:
                if heights[left] >= leftMax:
                    leftMax = heights[left]
                else:
                    totalWater += leftMax - heights[left]
                left += 1
            else:
                if heights[right] >= rightMax:
                    rightMax = heights[right]
                else:
                    totalWater += rightMax - heights[right]
                right -= 1
        return totalWater
                