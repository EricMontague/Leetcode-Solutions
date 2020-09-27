"""This file contains my solutions to Leetcode problem 844: Backspace String Compare."""


# time complexity: O(n + m), where 'n' is the length of the first string, and 'm' is
# the length of the second string
# space complexity: O(n + m)
class Solution:
    def backspaceCompare(self, string1: str, string2: str) -> bool:        
        stack1 = self.simulateTyping(string1)
        stack2 = self.simulateTyping(string2)
        return stack1 == stack2
    
    def simulateTyping(self, string):
        stack = []
        for character in string:
            if character == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(character)
        return stack


# Solution to the follow-up question
# time complexity: O(max(n, m)), where 'n' is the length of the first string, and 'm' is
# the length of the second string
# space complexity: O(1)

class Solution:
    def backspaceCompare(self, string1: str, string2: str) -> bool:        
        left = len(string1) - 1
        right = len(string2) - 1
        backspaces = [0, 0]
        while left >= 0 or right >= 0:
            while left >= 0 and (backspaces[0] > 0 or string1[left] == "#"):
                if string1[left] == "#":
                    backspaces[0] += 1
                else:
                    backspaces[0] -= 1
                left -= 1
            
            while right >= 0 and (backspaces[1] > 0 or string2[right] == "#"):
                if string2[right] == "#":
                    backspaces[1] += 1
                else:
                    backspaces[1] -= 1
                right -= 1
            if left >= 0 and right >= 0 and string1[left] == string2[right]:
                left -= 1
                right -= 1
            else:
                break
        return left == -1 and right == -1