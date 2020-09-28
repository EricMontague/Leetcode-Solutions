"""This file contains my solution to Leetcode problem 122: Best Time to Buy and Sell Stock II."""

# time complexity: O(n ^n), where 'n' is the number of integers in prices
# space complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = len(prices)
        return self.calcMaxProfit(prices, start, end)
    
    def calcMaxProfit(self, prices, start, end):
        maxProfit = 0
        if start > end:
            return maxProfit
        for currentDay in range(start, end):
            for futureDay in range(currentDay + 1, end):
                currentProfit = prices[futureDay] - prices[currentDay]
                maxFutureProfits = self.calcMaxProfit(prices, futureDay + 1, end)
                if currentProfit > 0:
                    maxProfit = max(maxProfit, currentProfit + maxFutureProfits)
                else:
                    maxProfit = max(maxProfit, maxFutureProfits)
        return maxProfit


# time complexity: O(n) where 'n' is the number of integers in prices
# space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentDay = 0
        numDays = len(prices)
        while currentDay < numDays - 1:
            while currentDay < numDays - 1 and prices[currentDay + 1] <= prices[currentDay]:
                currentDay += 1
            valley = prices[currentDay]
            
            while currentDay < numDays - 1 and prices[currentDay + 1] >= prices[currentDay]:
                currentDay += 1
            peak = prices[currentDay]
            maxProfit += peak - valley
        return maxProfit


# time complexity: O(n) where 'n' is the number of integers in prices
# space complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for currentDay in range(len(prices) - 1):
            if prices[currentDay + 1] > prices[currentDay]:
                maxProfit += prices[currentDay + 1] - prices[currentDay]
        return maxProfit
            