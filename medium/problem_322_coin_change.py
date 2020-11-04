"""This file contains my solutions to Leetcode problem 322: Coin Change."""




# Top down solution with Recursion
# time complexity: O(n * m), where 'n' is the amount and 'm' is the length of coins
# space comexplity: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        memo = [-1] * (amount + 1)
        min_coins = self.make_change(coins, amount, memo)
        if min_coins == float("inf"):
            return -1
        return min_coins
    
    def make_change(self, coins, remaining_amount, memo):
        if remaining_amount == 0:
            min_coins = 0
        elif memo[remaining_amount] >= 0:
            return memo[remaining_amount]
        else:
            min_coins = float("inf")
            for coin in coins:
                if coin <= remaining_amount:
                    result = self.make_change(coins, remaining_amount - coin, memo)
                    min_coins = min(min_coins, result + 1)
        memo[remaining_amount] = min_coins
        return memo[remaining_amount]
                    
        
# Bottom Up Solution
# time complexity: O(n * m), where 'n' is the total and 'm' is the length of coins
# space comexplity: O(n)        
class Solution2:
    def min_coins_to_make_change(self, coins, total):
        if not coins:
            return 0
        memo = [float("inf")] * (total + 1)
        memo[0] = 0
        for amount in range(1, total + 1):
            for coin in coins:
                if coin <= amount:
                    memo[amount] = min(memo[amount], 1 + memo[amount - coin])
        if memo[-1] == float("inf"):
            return -1
        return memo[-1]


# Naive Recursive Solution
# time complexity: O(N^ m), where 'N' is the total and 'm' is the length of coins
# space complexity: O(N)

class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        min_coins = self.make_change(coins, amount)
        if min_coins == float("inf"):
            return -1
        return min_coins
    
    def make_change(self, coins, remaining_amount):
        if remaining_amount == 0:
            min_coins = 0
        else:
            min_coins = float("inf")
            for coin in coins:
                if coin <= remaining_amount:
                    result = self.make_change(coins, remaining_amount - coin)
                    min_coins = min(min_coins, result + 1)
        return min_coins
                    
        
        
        