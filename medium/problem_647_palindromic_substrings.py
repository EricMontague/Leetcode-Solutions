"""This file contains my solutions to Leetcode problem 647: Palindromic Substrings"""

# Dynamic Programming Solution
# time complexity: O(n ^2), where 'n' is the number of characters in the string
# space complexity: O(n ^ 2), where 'n' is the number of characters in the string
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        stringLength = len(s)
        memo = [[False] * stringLength for index in range(stringLength)]
        start = 0
        for index in range(stringLength):
            start = 0
            end = index
            while end < stringLength:
                if start == end:
                    count += 1
                    memo[start][end] = True
                elif end == start + 1 and s[start] == s[end]:
                    count += 1
                    memo[start][end] = True
                elif s[start] == s[end] and memo[start + 1][end - 1]:
                    count += 1
                    memo[start][end] = True
                else:
                    memo[start][end] = False
                start += 1
                end += 1
        return count


# Space efficient solution
# time complexity: O(n ^2), where 'n' is the number of characters in the string
# space complexity: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        if s == "":
            return count
        for index in range(len(s)):
            numPalindromes1 = self.countPalindromes(
                s, index, index
            )
            numPalindromes2 = self.countPalindromes(
                s, index, index + 1
            )
            count += numPalindromes1 + numPalindromes2
        return count
    
    def countPalindromes(self, string, left, right):
        count = 0
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                return count
            count += 1
            left -= 1
            right += 1
        return count        
                

                