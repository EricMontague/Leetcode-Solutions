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
        if self.isPalindrome(string, start + 1, end, True):
            return True    
        return self.isPalindrome(string, start, end - 1, True)


# time complexity: O(n), where 'n' is the number of characters in the string
# space complexity: O(1)
class Solution:
    def validPalindrome(self, string: str) -> bool:
        return self.isPalindrome(string, "start") or self.isPalindrome(string, "end")
     
    
    def isPalindrome(self, string, pointer):
        start = 0
        end = len(string) - 1
        usedDeletion = False
        while start < end:
            if string[start] != string[end]:
                if usedDeletion:
                    return False
                if pointer == "start" and string[start + 1] == string[end]:
                    start += 1
                elif pointer == "end" and string[start] == string[end - 1]:
                    end -= 1
                else:
                    return False
                usedDeletion = True
            start += 1
            end -= 1
        return True