"""This file contains my solutions to Leetcode problem 213: House Robber II."""


# Bottom Up Space optimized
# time complexity: O(n), where 'n' is the length of houses
# space complexity: O(1)
class Solution:
    def rob(self, houses: List[int]) -> int:
        num_houses = len(houses)
        if num_houses == 1:
            return houses[0]
        return max(
            self.rob_houses(houses, 0, num_houses - 2),
            self.rob_houses(houses, 1, num_houses - 1)
        )
    
    def rob_houses(self, houses, start, end):
        num_houses = end - start + 1
        if num_houses == 1:
            return houses[start]
        two_ahead = houses[end]
        one_ahead = max(houses[end - 1], houses[end])
        for index in range(end - 2, start - 1, -1):
            current = max(
                houses[index] + two_ahead,
                one_ahead
            )
            two_ahead = one_ahead
            one_ahead = current
        return one_ahead

# Bottom Up + Memoization
# time complexity: O(n), where 'n' is the length of houses
# space complexity: O(n), where 'n' is the length of houses
class Solution:
    def rob(self, houses: List[int]) -> int:
        num_houses = len(houses)
        if num_houses == 1:
            return houses[0]
        return max(
            self.rob_houses(houses, 0, num_houses - 2),
            self.rob_houses(houses, 1, num_houses - 1)
        )
    
    def rob_houses(self, houses, start, end):
        num_houses = end - start + 1
        if num_houses == 1:
            return houses[start]
        memo = [-1] * len(houses)
        memo[end] = houses[end]
        memo[end - 1] = max(houses[end - 1], houses[end])
        for index in range(end - 2, start - 1, -1):
            memo[index] = max(
                houses[index] + memo[index + 2],
                memo[index + 1]
            )
        if end == len(houses) - 1:
            return memo[1]
        return memo[0]


# Recursion + Memoization
# time complexity: O(n), where 'n' is the length of houses
# space complexity: O(n), where 'n' is the length of houses
class Solution:
    def rob(self, houses: List[int]) -> int:
        num_houses = len(houses)
        if num_houses == 1:
            return houses[0]
        memo1 = [-1] * num_houses
        memo2 = [-1] * num_houses
        return max(
            self.rob_houses(houses, 0, memo1, 0, len(houses) - 2),
            self.rob_houses(houses, 1, memo2, 1, len(houses) - 1)
        )
    
    def rob_houses(self, houses, index, memo, start, end):
        if index > end:
            return 0
        elif memo[index] >= 0:
            return memo[index]
        memo[index] = max(
            houses[index] + self.rob_houses(houses, index + 2, memo, start, end),
            self.rob_houses(houses, index + 1, memo, start, end)
        )
        return memo[index]


    