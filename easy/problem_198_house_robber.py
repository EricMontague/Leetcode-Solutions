"""THis file contains my solutions to Leetcode problem 198: House Robber."""

# Bottom Up Solution Space Optimized
# time complexity: O(n), where 'n' is the number of houses
# space complexity: O(1)
class Solution:
    def rob(self, houses: List[int]) -> int:
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        before_previous = houses[0]
        previous = max(houses[0], houses[1])
        for index in range(2, len(houses)):
            current = max(previous, before_previous + houses[index])
            before_previous = previous
            previous = current
        return previous

# Bottom Up Solution
# time complexity: O(n), where 'n' is the number of houses
# space complexity: O(n)
class Solution:
    def rob(self, houses: List[int]) -> int:
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        memo = [None] * len(houses)
        memo[0] = houses[0]
        memo[1] = max(houses[0], houses[1])
        for index in range(2, len(houses)):
            memo[index] = max(
                memo[index - 1],
                memo[index - 2] + houses[index]
            )
        return memo[-1]

# Recursion + Memoization
# time complexity: O(n), where 'n' is the number of houses
# space complexity: O(n)
class Solution:
    def rob(self, houses: List[int]) -> int:
        memo = [None] * len(houses)
        return self.rob_houses(houses, memo, len(houses) - 1)
    
    def rob_houses(self, houses, memo, index):
        if index < 0:
            return 0
        if memo[index] is not None:
            return memo[index]
        max_amount = max(
            self.rob_houses(houses, memo, index - 1),
            self.rob_houses(houses, memo, index - 2) + houses[index]
        )
        memo[index] = max_amount
        return memo[index]




# Naive Recursive solution
# time complexity: O(2 ^n), where 'n' is the number of houses
# space complexity: O(n)
class Solution:
    def rob(self, houses: List[int]) -> int:
        return self.rob_houses(houses, len(houses) - 1)
    
    def rob_houses(self, houses, index):
        if index < 0:
            return 0
        max_amount = max(
            self.rob_houses(houses, index - 1),
            self.rob_houses(houses, index - 2) + houses[index]
        )
        return max_amount
        