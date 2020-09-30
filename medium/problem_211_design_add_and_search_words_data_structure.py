"""This file contains my solution to Leetcode problem 211: Design Add
And Search Words Data Structure.
"""

# time complexity: 
# addWord() - O(n), where 'n' is the length of the word
# search() -

# space complexity:
# addWord() - O(n)
# search() = O(n)

class TrieNode:
    
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = [None] * 26
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        if word:
            current = self.root
            for character in word:
                mappedIndex = ord(character) - ord("a")
                if not current.children[mappedIndex]:
                    current.children[mappedIndex] = TrieNode()
                current = current.children[mappedIndex]
            current.end_of_word = True
    
    def search(self, word):
        if not word:
            return False
        return self._search(self.root, word, 0)
    
    def _search(self, current, word, index):
        if index == len(word):
            if current.end_of_word:
                return True
            return False
        character = word[index]
        if character == ".":
            for child in current.children:
                if child and self._search(child, word, index + 1):
                    return True
            return False
        else:
            mappedIndex = ord(character) - ord("a")
            if not current.children[mappedIndex]:
                return False
            return self._search(current.children[mappedIndex], word, index + 1)
        
        

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)