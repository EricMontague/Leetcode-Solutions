"""This file contains my solution to Leetcode problem 389: Find the Difference."""

# time complexity: O(n + m), where 'n' is the length of the first string and 'm' is the
# length of the second string
# space complexity: O(1)
class Solution:
    def findTheDifference(self, originalString: str, randomizedString: str) -> str:
        characterCounts = self.buildCharacterFrequencyArray(randomizedString)
        for character in originalString:
            index = self.mapCharacterToIndex(character, "a")
            characterCounts[index] -= 1
        for index, characterCount in enumerate(characterCounts):
            if characterCount == 1:
                characterAscii = self.mapIndexToCharacter(index, "a")
                return chr(characterAscii)
    
    def buildCharacterFrequencyArray(self, string):
        characterCounts = [0] * 26
        for character in string:
            index = self.mapCharacterToIndex(character, "a")
            characterCounts[index] += 1
        return characterCounts
    
    def mapCharacterToIndex(self, character, base):
        return ord(character) - ord(base)
    
    def mapIndexToCharacter(self, index, base):
        return index + ord(base)