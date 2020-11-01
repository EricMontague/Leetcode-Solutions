"""This problem contains my solutions to Leetcode problem 746: Min Cost Climbing Stairs.

Recurrence Relation
-------------------

f(i) = costs[i], if i == 0 or i == 1
f(i) = costs[i] + min(f(i - 1), f(i - 2)), if i > 1
"""



# Bottom Up Space Efficient
# time complexity: O(n), where 'n' is the length of costs
# space complexity: O(1)
class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        if not costs:
            return 0
        if len(costs) == 1:
            return costs[0]
        min_cost_before_previous = costs[0]
        min_cost_previous = costs[1]
        for index in range(2, len(costs)):
            min_cost_current = costs[index] + min(
                min_cost_before_previous,
                min_cost_previous
            )
            min_cost_before_previous = min_cost_previous
            min_cost_previous = min_cost_current
        return min(min_cost_before_previous, min_cost_previous)

# Bottom Up with memoization
# time complexity: O(n), where 'n' is the length of costs
# space complexity: O(n)
class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        if not costs:
            return 0
        if len(costs) == 1:
            return costs[0]
        min_costs = [-1] * len(costs)
        min_costs[0] = costs[0]
        min_costs[1] = costs[1]
        for index in range(2, len(costs)):
            min_costs[index] = costs[index] + min(
                min_costs[index - 1],
                min_costs[index - 2]
            )
        return min(min_costs[-1], min_costs[-2])


# Recursion + Memoization
# time complexity: O(n), where 'n' is the length of costs
# space complexity: O(n)
class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        memo = [-1] * len(costs)
        min_cost = self.min_cost(costs, len(costs) - 1, memo)
        return min(min_cost, memo[-2])
    
    def min_cost(self, costs, index, memo):
        if index < 0:
            return 0
        if index == 0 or index == 1:
            cost = costs[index]
        elif memo[index] >= 0:
            return memo[index]
        else:
            cost = min(
                self.min_cost(costs, index - 1, memo),
                self.min_cost(costs, index - 2, memo)
            ) + costs[index]
        memo[index] = cost
        return memo[index]


# Naive Recursive Solution
# time complexity: O(2 ^ n)
# space complexity: O(n)
class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        return min(
            self.min_cost(costs, len(costs) - 1),
            self.min_cost(costs, len(costs) - 2)
        )
    
    def min_cost(self, costs, index):
        if index < 0:
            return 0
        if index == 0 or index == 1:
            return costs[index]
        cost = min(
            self.min_cost(costs, index - 1),
            self.min_cost(costs, index - 2)
        )
        return cost + costs[index]