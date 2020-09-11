"""This file contains my solutions to Leetcode problem 49: Group Anagrams."""

# time complexity: O(nm), where 'n' is the length of the strings list and
# 'm' is the length of the longest string

# space complexity: O(n), where 'n' is the length of the strings list

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []
        stringGroups = self.groupStringsByCharacterFrequency(strings)
        return stringGroups.values()
    
    def groupStringsByCharacterFrequency(self, strings):
        stringGroups = defaultdict(list)
        for string in strings:
            characterFrequencyTuple = tuple(
                self.buildCharacterFrequencyList(string)
            )
            stringGroups[characterFrequencyTuple].append(string)
        return stringGroups
    
    def buildCharacterFrequencyList(self, string):
        base = ord("a")
        characterCounts = [0] * 26
        for character in string:
            asciiValue = ord(character)
            characterCounts[asciiValue - base] += 1
        return characterCounts


# Alternate solution - not as efficient
# time complexity: O(nmlogm), where 'n' is the length of the strings list and
# 'm' is the length of the longest string

# space complexity: O(n m), where 'n' is the length of the strings list
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []
        sortedStringGroups = self.groupStringsBySortOrder(strings)
        return sortedStringGroups.values()
    
    def groupStringsBySortOrder(self, strings):
        sortedStringGroups = defaultdict(list)
        for string in strings:
            sortedStringTuple = tuple(sorted(string))
            sortedStringGroups[sortedStringTuple].append(string)
        return sortedStringGroups
    
    