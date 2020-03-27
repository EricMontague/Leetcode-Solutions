"""This is my solution to problem 500."""


#Overall time complexity: O(n + m), where "n" is the number of words in the
#input list and "m" is the total number of characters between all of the words
#Overall space complexity is O(n), where "n" is the number of words in the input list
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        validWords = []
        if not words:
            return validWords
        keyboardRows = {
            "q": 0, "w": 0, "e": 0, "r": 0, "t": 0, "y": 0,
            "u": 0, "i": 0, "o": 0, "p": 0, "a": 1, "s": 1,
            "d": 1, "f": 1, "g": 1, "h": 1, "j": 1, "k": 1,
            "l": 1, "z": 2, "x": 2, "c": 2, "v": 2, "b": 2,
            "n": 2, "m": 2
        }
        for word in words:
            if self.isValidWord(word.lower(), keyboardRows):
                validWords.append(word)
        return validWords
    
    def isValidWord(self, word, keyboardRows):
        row = keyboardRows[word[0]]
        for index in range(1, len(word)):
            if keyboardRows[word[index]] != row:
                return False
        return True

        