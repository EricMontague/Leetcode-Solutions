"""This file contains my solution for leetcode problem 76: Minimum Window substring."""

# time complexity: O(n + m), where 'n' is string and 'm' is chars
# space complexity: O(m), where 'm' is chars
from collections import Counter

class Solution:
    def minWindow(self, string: str, chars: str) -> str:
        if string == "" or chars == "" or len(chars) > len(string):
            return ""
        foundValidWindow = False
        charCounts = Counter(chars)
        minSubstringStart = 0
        minSubstringEnd = len(string) - 1
        windowStart = 0
        uniqueCount = len(chars)
        for windowEnd in range(len(string)):
            endChar = string[windowEnd]
            if endChar in charCounts:
                charCounts[endChar] -= 1
                if charCounts[endChar] >= 0:
                    uniqueCount -= 1
                while uniqueCount == 0:
                    if windowEnd - windowStart <= minSubstringEnd - minSubstringStart:
                        foundValidWindow = True
                        minSubstringEnd = windowEnd
                        minSubstringStart = windowStart
                    startChar = string[windowStart]
                    if startChar in charCounts:
                        charCounts[startChar] += 1
                        if charCounts[startChar] > 0:
                            uniqueCount += 1
                    windowStart += 1
                    while windowStart < windowEnd and string[windowStart] not in charCounts:
                        windowStart += 1
        if not foundValidWindow:
            return ""
        return string[minSubstringStart: minSubstringEnd + 1]