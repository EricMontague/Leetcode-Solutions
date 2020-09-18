"""This file contains my solution to Leetcode problem 424:
Longest Repeating Character Replacement
"""

# time complexity: O(n), where 'n' is the number of characters in string
# space complexity: O(1)

class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        maxLength = 0
        if not string:
            return maxLength
        maxCount = 0
        windowStart = 0
        charCounts = [0] * 26
        arrayBase = ord("A")
        for windowEnd in range(len(string)):
            endChar = string[windowEnd]
            currentCount = charCounts[ord(endChar) - arrayBase]
            charCounts[ord(endChar) - arrayBase] = currentCount + 1
            maxCount = max(maxCount, currentCount + 1)
            
            while (windowEnd - windowStart + 1) - maxCount > k:
                startChar = string[windowStart]
                charCounts[ord(startChar) - arrayBase] -= 1
                windowStart += 1
                maxCount = max(charCounts)
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        return maxLength