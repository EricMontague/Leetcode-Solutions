"""This file contains my solution to Leetcode problem 5: Longest Palindromic Substring."""


class Solution:  

    def longestPalindrome(self, string: str) -> str:
        start = 0
        end = 0
        # memo = [[] * len(string) for index in range(len(string))]
        for i in range(len(string)):
            length1 = self.expandAroundCenter(string, i, i)
            length2 = self.expandAroundCenter(string, i, i + 1)
            maxLength = max(length1, length2)
            if maxLength > end - start:
                if maxLength % 2 == 0:
                    mid = maxLength // 2
                    start = i - mid + 1
                    end = i + mid
                else:
                    mid = maxLength // 2
                    start = i - mid
                    end = i + mid
        return string[start: end + 1]
    
    def expandAroundCenter(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    