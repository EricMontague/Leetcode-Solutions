"""This file contains my solution to Leetcode problem 208: Implement Trie."""

# All methods run in O(n) time, where 'n' is the size of the input string
# All methods run in O(1) space

class TrieNode:
    
    CHARACTER_SET_SIZE = 26
    
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = [None] * self.CHARACTER_SET_SIZE

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.character_base = ord("a")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word:
            current = self.root
            for character in word:
                mappedIndex = ord(character) - self.character_base
                if current.children[mappedIndex] is None:
                    current.children[mappedIndex] = TrieNode()
                current = current.children[mappedIndex]
            current.end_of_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.findPrefix(word)
        if node is None or not node.end_of_word:
            return False
        return True
    
    def findPrefix(self, word):
        if not word:
            return None
        current = self.root
        for character in word:
            mappedIndex = ord(character) - self.character_base
            if current.children[mappedIndex] is None:
                return None
            current = current.children[mappedIndex]
        return current
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.findPrefix(prefix)
        return node is not None
        


