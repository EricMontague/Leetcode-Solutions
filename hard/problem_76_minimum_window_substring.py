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



# More optimized solution for the case where "t" is much smaller than "s".
# Same time and space complexities

class Solution:
    def minWindow(self, string: str, chars: str) -> str:
        if not string or not chars or len(chars) > len(string):
            return ""
        charCounts = self.buildCharacterFrequencyTable(chars)
        filteredStringArray = self.buildFilteredStringArray(string, charCounts)
        uniqueCounts = len(chars)
        foundMinWindow = False
        left = 0
        right = 0
        minStart = 0
        minEnd = len(string) - 1
        while right < len(filteredStringArray):
            endChar = filteredStringArray[right][0]
            charCounts[endChar] -= 1
            if charCounts[endChar] >= 0:
                uniqueCounts -= 1
            while left <= right and uniqueCounts == 0:
                foundMinWindow = True
                end = filteredStringArray[right][1]
                start = filteredStringArray[left][1]
                if end - start < minEnd - minStart:
                    minEnd = end
                    minStart = start
                startChar = filteredStringArray[left][0]
                if startChar in charCounts:
                    charCounts[startChar] += 1
                    if charCounts[startChar] > 0:
                        uniqueCounts += 1
                left += 1
            right += 1
        if not foundMinWindow:
            return ""
        return string[minStart: minEnd + 1]
    
    def buildCharacterFrequencyTable(self, chars):
        charCounts = {}
        for char in chars:
            if char not in charCounts:
                charCounts[char] = 0
            charCounts[char] += 1
        return charCounts
    
    def buildFilteredStringArray(self, string, charCounts):
        filteredStringArray = [
            (char, idx) for idx, char in enumerate(string) if char in charCounts
        ]
        return filteredStringArray
        
            