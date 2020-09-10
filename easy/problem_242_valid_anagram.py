"""This file contains my solution to Leetcode problem 242: Valid Anagram."""


# time complexity: O(n), where 'n' is the number of characters in originalString or anagram
# space complexity: O(1)
from collections import defaultdict

class Solution:
    def isAnagram(self, originalString: str, anagram: str) -> bool:
        if len(originalString) != len(anagram):
            return False
        characterCounts = self.countCharacterDifferences(originalString, anagram)
        return self.hasEqualCount(characterCounts)
    
    def countCharacterDifferences(self, originalString, anagram):
        characterCounts = defaultdict(int)
        for index in range(len(originalString)):
            originalCharacter = originalString[index]
            anagramCharacter = anagram[index]
            characterCounts[originalCharacter] += 1
            characterCounts[anagramCharacter] -= 1
        return characterCounts
    
    def hasEqualCount(self, characterCounts):
        for character in characterCounts:
            if characterCounts[character] != 0:
                return False
        return True