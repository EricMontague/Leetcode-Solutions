"""This file contains my solution to Leetcode problem 5: Longest Palindromic Substring."""


# Time complexity: O(n ^ 2), where 'n' is the number of characters in the string
# Space complexity: O(1)
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
    
    

# Dynamic Programming solution
# Time complexity: O(n ^ 2), where 'n' is the number of characters in the string
# Space complexity: O(n ^ 2), where 'n' is the number of characters in the string
class Solution:  

    def longestPalindrome(self, string: str) -> str:
        start = 0
        end = 0
        memo = [[False] * len(string) for index in range(len(string))]
        for i in range(len(string)):
            length1 = self.expandAroundCenter(string, i, i, memo)
            length2 = self.expandAroundCenter(string, i, i + 1, memo)
            maxLength = max(length1, length2)
            if maxLength > end - start:
                mid = maxLength // 2
                if maxLength % 2 == 0:
                    start = i - mid + 1
                    end = i + mid
                else:
                    start = i - mid
                    end = i + mid
        return string[start: end + 1]
    
    def expandAroundCenter(self, string, i, j, memo):
        if i < 0 or j >= len(string):
            return 0
        if string[i] != string[j]:
            memo[i][j] = False
            return 0
        if i == j: # one character at center
            memo[i][j] = True
        if j == i + 1 and string[i] == string[j]: # two characters at center
            memo[i][j] = True
        if memo[i + 1][j - 1] and string[i] == string[j]: 
            memo[i][j] = True
        return max(j - i + 1, self.expandAroundCenter(string, i - 1, j + 1, memo))
        
       