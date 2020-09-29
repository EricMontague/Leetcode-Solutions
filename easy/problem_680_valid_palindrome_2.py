"""This file contains my solutions to Leetcode problem 680: Valid Palindrome II."""


# time complexity: O(n), where 'n' is the number of characters in the string
# space complexity: O(n)
class Solution:
    def validPalindrome(self, string: str) -> bool:
        return self.isPalindrome(string, 0, len(string) - 1, False)
    
    def isPalindrome(self, string, start, end, usedDeletion):
        if start >= end:
            return True
        if string[start] == string[end]:
            return self.isPalindrome(string, start + 1, end - 1, usedDeletion)
        if usedDeletion:
            return False
        return (
            self.isPalindrome(string, start + 1, end, True) 
            or self.isPalindrome(string, start, end - 1, True)
        )


# time complexity: O(n), where 'n' is the number of characters in the string
# space complexity: O(1)
class Solution:
    def validPalindrome(self, string: str) -> bool:
        start = 0
        end = len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return self.isPalindrome(string, start + 1, end) or self.isPalindrome(string, start, end - 1)
            start += 1
            end -= 1
        return True
    
    def isPalindrome(self, string, start, end):
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True