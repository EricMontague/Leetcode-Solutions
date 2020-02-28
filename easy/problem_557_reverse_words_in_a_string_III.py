"""My solutions to problem 557: Reverse Words in a String III"""

#initial solution
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for index in range(len(s) - 1, -1, -1):
            if s[index] != " ":
                word += s[index]
            else:
                words.append(word)
                word = ""
        words.append(word)
        return " ".join(reversed(words))


#A more modularized solution without relying on the built-in
#reverse and join methods
class Solution:
    def reverseWords(self, s: str) -> str:
        words = self.reverse_letters(s)
        self.reverse_word_list(words)
        return self.join_word_list(words)
    
    def reverse_letters(self, s):
        """Reverse the letters in each word in the input
        string and add them to a list. Return the list 
        afterwards.
        """
        words = []
        word = ""
        for index in range(len(s) - 1, -1, -1):
            if s[index] != " ":
                word += s[index]
            else:
                words.append(word)
                word = ""
        words.append(word)
        return words
    
    def reverse_word_list(self, words):
        """Reverse the word list in place."""
        low = 0
        high = len(words) - 1
        while low < high:
            words[low], words[high] = words[high], words[low]
            low += 1
            high -= 1
    
    def join_word_list(self, words):
        """Return the list of words joined by spaces."""
        string = ""
        for index, word in enumerate(words):
            if index != len(words) - 1:
                string += word + " "
            else:
                string += word
        return string
    

#One-linter solution
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s[::-1].split()))


#Overall time complexity of all solutions is O(n)
#Overall space complexity of all solutions is O(n)
