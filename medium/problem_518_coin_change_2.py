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

# Bottom Up Solution Space Optimized
# time complexity: O(n * m), where 'n' is the number of coins and 'm' is the amount
# space complexity: O(m)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total_coins = len(coins)
        combinations = [0] * (amount + 1)
        combinations[0] = 1
        for num_coins in range(total_coins):
            for remaining_amount in range(amount + 1):
                coin_value = coins[num_coins - 1]
                combo1 = combinations[remaining_amount]
                combo2 = 0
                if coin_value <= remaining_amount:
                    combo2 = combinations[remaining_amount - coin_value]
                combinations[remaining_amount] = combo1 + combo2
        return combinations[amount]

# Bottom Up Solution
# Recursion with Memoization
# time complexity: O(n * m), where 'n' is the number of coins and 'm' is the amount
# space complexity: O(n * m)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total_coins = len(coins)
        combinations = [
            [None] * (amount + 1)
            for coin in range(total_coins + 1)
        ]
        for num_coins in range(total_coins + 1):
            for remaining_amount in range(amount + 1):
                if remaining_amount == 0:
                    combinations[num_coins][remaining_amount] = 1
                elif num_coins == 0:
                    combinations[num_coins][remaining_amount] = 0
                else:
                    coin_value = coins[num_coins - 1]
                    combo1 = combinations[num_coins - 1][remaining_amount]
                    combo2 = 0
                    if coin_value <= remaining_amount:
                        combo2 = combinations[num_coins][remaining_amount - coin_value]
                    combinations[num_coins][remaining_amount] = combo1 + combo2
        return combinations[total_coins][amount]

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
    
    # O(n + m)
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