"""This script contains my solution for Leetcode problem 807."""


#Overall time complexity: O(n ^ 2)
#Overall space complexity: O(n)
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxRowValues = [0] * len(grid)
        maxColValues = [0] * len(grid[0])
        self.getMaxValues(grid, maxRowValues, maxColValues)
        return self.findMaxIncrease(grid, maxRowValues, maxColValues)
    
    def getMaxValues(self, grid, maxRowValues, maxColValues):
        for rowIndex, row in enumerate(grid):
            for colIndex, colValue in enumerate(row):
                maxRowValues[rowIndex] = max(maxRowValues[rowIndex], colValue)
                maxColValues[colIndex] = max(maxColValues[colIndex], colValue)
    
    def findMaxIncrease(self, grid, maxRowValues, maxColValues):
        maxIncrease = 0
        for rowIndex, row in enumerate(grid):
            for colIndex, colValue in enumerate(row):
                maxIncrease += min(maxRowValues[rowIndex], maxColValues[colIndex]) - colValue
        return maxIncrease

        