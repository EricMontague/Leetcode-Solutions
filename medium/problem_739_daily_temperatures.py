"""This file contains a solution from Leetcode problem 739: Daily Temperatures."""

# time complexity: O(n), where 'n' is the number of temperatures
# space complexity: O(n), where 'n' is the number of temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return temperatures
        numTemps = len(temperatures)
        daysUntilWarmerTemps = [0] * numTemps
        stack = []
        for currentIndex in range(numTemps):
            while stack and temperatures[currentIndex] > temperatures[stack[-1]]:
                previousIndex = stack.pop()
                daysUntilWarmerTemps[previousIndex] = currentIndex - previousIndex
            stack.append(currentIndex)
        return daysUntilWarmerTemps