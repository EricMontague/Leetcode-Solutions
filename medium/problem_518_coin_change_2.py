"""This file contains my solutions to Leetcode problem 518: Coin Change 2.

Recurrence Relation
------------------
f(c, A, i) = 0, if len(c) == 0 or if A < 0
f(c, A, i) = 1, if A == 0
f(c, A, i) = f(c, A - c[i], i) + f(c, A, i - 1)

- c == coins
- A == amount
- i == index of coin to choose

"""



# Recursion with Memoization
# time complexity: O(n * m), where 'n' is the number of coins and 'm' is the amount
# space complexity: O(n * m)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinations = [
            [None] * (amount + 1)
            for coin in range(len(coins) + 1)
        ]    
        combos = self.compute_combinations(
            amount, 
            coins, 
            len(coins) - 1,
            combinations
        )
        return combos
    
    def compute_combinations(self, amount, coins, index, combos):
        if combos[index + 1][amount] is not None:
            return combos[index + 1][amount]
        elif amount == 0:
            num_combos = 1
        elif index == -1:
            num_combos = 0
        else:
            combo1 = 0
            coin = coins[index]
            if coin <= amount:
                combo1 = self.compute_combinations(
                    amount - coin, 
                    coins, 
                    index,
                    combos
                )
            combo2 = (
                self.compute_combinations(amount, coins, index - 1, combos)
            )
            num_combos = combo1 + combo2
        combos[index + 1][amount] = num_combos
        return num_combos


# Naive Recursive Solution
# time complexity: O(2 ^ (n + m)), where 'n' is the number of coins and 'm' is the amount
# space complexity: O(n + m), where 'n' is the number of coins and 'm' is the amount
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.compute_combinations(amount, coins, len(coins) - 1)
    
    def compute_combinations(self, amount, coins, index):
        if index == -1 or amount < 0:
            return 0
        if amount == 0:
            return 1
        combinations = (
            self.compute_combinations(amount, coins, index - 1)
            + self.compute_combinations(amount - coins[index], coins, index)
        )
        return combinations