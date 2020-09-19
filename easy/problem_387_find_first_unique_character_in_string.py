"""this file contains my solution to Leetcode problem 387: Find First Unique Character in String."""

# time complexity: O(n), where 'n' is the number of characters in the string
# space complexity: O(1)
class Solution:
    def firstUniqChar(self, string: str) -> int:
        charCounts = self.buildFrequencyList(string)
        return self.findFirstUniqChar(charCounts, string)
    
    def buildFrequencyList(self, string):
        charCounts = [0] * 26
        for index, char in enumerate(string):
            charCounts[ord(char) - ord("a")] += 1
        return charCounts
    
    def findFirstUniqChar(self, charCounts, string):
        for index, char in enumerate(string):
            if charCounts[ord(char) - ord("a")] == 1:
                return index
        return -1
            
        
        