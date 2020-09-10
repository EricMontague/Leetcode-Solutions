"""This file contains my solution to Leetcode problem 20: Valid Parentheses."""

# time complexity: O(n), where 'n' is the number of parentheses
# space complexity: O(n), where 'n' is the number of parentheses
class Solution:
    def isValid(self, parentheses: str) -> bool:
        parenthesisMapping = {"]": "[", "}": "{", ")": "("}
        stack = []
        for parenthesis in parentheses:
            if parenthesis in parenthesisMapping:
                if stack and stack[-1] == parenthesisMapping[parenthesis]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parenthesis)
        return not stack
