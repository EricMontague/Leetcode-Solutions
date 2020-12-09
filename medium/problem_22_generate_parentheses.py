"""This file contains my solutions to Leetcode problem 22: Generate Parentheses."""


# Backtracking Solution
class Solution:
    def generateParenthesis(self, num_pairs: int) -> List[str]:
        if num_pairs == 0:
            return []
        final_parentheses = []
        current_parentheses = []
        self.generate_combinations(
            num_pairs, 
            num_pairs, 
            current_parentheses, 
            final_parentheses
        )
        return final_parentheses
    
    def generate_combinations(self, num_open, num_closed, current, final):
        if num_open == 0 and num_closed == 0:
            final.append("".join(current))
        else:
            if num_open > 0:
                current.append("(")
                self.generate_combinations(
                    num_open - 1, num_closed, current, final
                )
                current.pop()
            if num_closed > num_open:
                current.append(")")
                self.generate_combinations(
                    num_open, num_closed - 1, current, final
                )
                current.pop()


# Iterative DFS solution

class Solution:
    def generateParenthesis(self, num_pairs: int) -> List[str]:
        if num_pairs == 0:
            return []
        final_parentheses = []
        stack = [("", num_pairs, num_pairs)]
        while stack:
            current_parentheses, num_open, num_closed = stack.pop()
            if num_open == 0 and num_closed == 0:
                final_parentheses.append(current_parentheses)
            else:
                if num_open > 0:
                    stack.append(
                        (current_parentheses + "(", num_open - 1, num_closed)
                    )
                if num_closed > num_open:
                    stack.append(
                        (current_parentheses + ")", num_open, num_closed - 1)
                    )
        return final_parentheses


#BFS Solution
from collections import deque

class Solution:
    def generateParenthesis(self, num_pairs: int) -> List[str]:
        if num_pairs == 0:
            return []
        final_parentheses = []
        queue = deque([("", num_pairs, num_pairs)])
        while queue:
            current_parentheses, num_open, num_closed = queue.popleft()
            if num_open == 0 and num_closed == 0:
                final_parentheses.append(current_parentheses)
            else:
                if num_open > 0:
                    queue.append(
                        (current_parentheses + "(", num_open - 1, num_closed)
                    )
                if num_closed > num_open:
                    queue.append(
                        (current_parentheses + ")", num_open, num_closed - 1)
                    )
        return final_parentheses