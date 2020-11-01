"""This file contains my solutions for Leetcode problem 70: Climbing Stairs.

Recurrence Relation
-------------------

F(s) = 1, if s == n - 1, or s == n
F(s) = F(s + 1) + F(s + 2), 0 <= s < n - 1

'n' is the number of steps
"""


# Bottom Up Solution space optimized
# time complexity: O(n), where 'n' is the number of steps
# space complexity: O(1)
class Solution:
    def climbStairs(self, num_steps: int) -> int:
        if num_steps == 0 or num_steps == 1:
            return num_steps
        two_steps_ahead = 1
        one_step_ahead = 2
        for step in range(num_steps - 3, -1, -1):
            current_step = (
                one_step_ahead
                + two_steps_ahead
            )
            two_steps_ahead = one_step_ahead
            one_step_ahead = current_step
        return one_step_ahead
        

# Bottom Up Solution
# time complexity: O(n), where 'n' is the number of steps
# space complexity: O(n)
class Solution:
    def climbStairs(self, num_steps: int) -> int:
        if num_steps == 0 or num_steps == 1:
            return num_steps
        memo = [0] * num_steps
        memo[num_steps - 1] = 1
        memo[num_steps - 2] = 2
        for step in range(num_steps - 3, -1, -1):
            memo[step] = memo[step + 1] + memo[step + 2]
        return memo[0]


# Recursion with Memoization
# time complexity: O(n), where 'n' is the number of steps
# space complexity: O(n)
class Solution:
    def climbStairs(self, num_steps: int) -> int:
        memo = [0] * (num_steps + 1)
        return self.num_ways_to_top(0, num_steps, memo)
    
    def num_ways_to_top(self, current_step, num_steps, memo):
        if memo[current_step] > 0:
            return memo[current_step]
        if current_step in (num_steps - 1, num_steps):
            num_ways = 1
        else:
            num_ways = (
                self.num_ways_to_top(current_step + 1, num_steps, memo)
                + self.num_ways_to_top(current_step + 2, num_steps, memo)
            )
        memo[current_step] = num_ways
        return memo[current_step]



# Naive Recursion
# time complexity: O(2^n), where 'n' is the number of steps
# space complexity: O(n)
class Solution:
    def climbStairs(self, num_steps: int) -> int:
        return self.num_ways_to_top(0, num_steps)
    
    def num_ways_to_top(self, current_step, num_steps):
        if current_step in (num_steps - 1, num_steps):
            return 1
        return (
            self.num_ways_to_top(current_step + 1, num_steps)
            + self.num_ways_to_top(current_step + 2, num_steps)
        )
        