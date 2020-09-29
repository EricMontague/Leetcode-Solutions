"""This file contains my solution for problem 125 - Valid Palindrome."""


# Overall time complexity: O(n), where 'n' is the number of characters in the string
# Overall space complexity is O(1)
class Solution:
    def isPalindrome(self, string: str) -> bool:
        start = 0
        end = len(string) - 1
        while start < end:
            while start < end and not string[start].isalnum():
                start += 1
            while start < end and not string[end].isalnum():
                end -= 1
            if string[start].lower() != string[end].lower():
                return False
            start += 1
            end -= 1
        return True



# Recursive solution
# Overall time complexity: O(n), where 'n' is the number of characters in the string
# Overall space complexity is O(n)
class Solution:
    def isPalindrome(self, string: str) -> bool:
        start = 0
        end = len(string) - 1
        return self._isPalindrome(string, start, end)
    
    def _isPalindrome(self, string, start, end):
        if start >= end:
            return True
        if not string[start].isalnum():
            return self._isPalindrome(string, start + 1, end)
        if not string[end].isalnum():
            return self._isPalindrome(string, start, end - 1)
        if string[start].lower() != string[end].lower():
            return False
        return self._isPalindrome(string, start + 1, end - 1)
