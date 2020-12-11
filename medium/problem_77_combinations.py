"""This file contains my solution to Leetcode problem 77."""


# This is an 'n' choose 'k' problem, which is the number of ways to
# choose 'k' elements from a set of size 'n'

# time complexity: O(n!/ k!*(n-k)!) * k, where 'n' is num and 'k' is 
# combination_size

# space complexity: O(n!/ k!*(n-k)!) * k
class Solution:
    def combine(self, num: int, combination_size: int) -> List[List[int]]:
        current_comnbinations = []
        final_combinations = []
        self.generate_combinations(
            num, 1, combination_size, current_comnbinations, final_combinations
        )
        return final_combinations
    
    def generate_combinations(self, n, start, remaining, current, final):
        if remaining == 0:
            final.append(current.copy())
        else:
            for num in range(start, n - remaining + 2):
                current.append(num)
                self.generate_combinations(
                    n,
                    num + 1,
                    remaining - 1,
                    current,
                    final
                )
                current.pop()