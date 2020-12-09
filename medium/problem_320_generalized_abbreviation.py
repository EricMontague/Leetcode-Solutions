"""This file contains my solutions for Leetcode problem 320: Generalized Abbreviation."""


# Backtracking Solution
# time complexity: O(N * 2^N), where 'N' is the length of word
# space complexity: O(N * 2^N)
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if not word:
            return [""]
        abbreviations = []
        abbreviation = []
        num_abbreviated = 0
        start_index = 0
        self.create_abbreviations(
            word,
            start_index,
            num_abbreviated,
            abbreviation,
            abbreviations
        )
        return abbreviations
    
    def create_abbreviations(
        self,
        word,
        index,
        num_abbreviated,
        current_abbreviation,
        abbreviations
    ):
        if index == len(word):
            if num_abbreviated > 0:
                current_abbreviation.append(str(num_abbreviated))
            abbreviations.append("".join(current_abbreviation))
            if num_abbreviated != 0:
                current_abbreviation.pop()
        else:
            self.create_abbreviations(
                word,
                index + 1,
                num_abbreviated + 1,
                current_abbreviation,
                abbreviations
            )
            if num_abbreviated > 0:
                current_abbreviation.append(str(num_abbreviated))
            current_abbreviation.append(word[index])
            self.create_abbreviations(
                word,
                index + 1,
                0,
                current_abbreviation,
                abbreviations
            )
            current_abbreviation.pop()
            if num_abbreviated > 0:
                current_abbreviation.pop()


# Iterative DFS Solution

class Abbreviation:
    
    def __init__(self, string, count, index):
        self.string = string
        self.count = count
        self.index = index

        
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        abbreviations = []
        stack = [Abbreviation("", 0, 0)]
        while stack:
            current_abbreviation = stack.pop()
            if current_abbreviation.index == len(word):
                if current_abbreviation.count > 0:
                    current_abbreviation.string += str(current_abbreviation.count)
                abbreviations.append(current_abbreviation.string)
            else:
                stack.append(
                    Abbreviation(
                        current_abbreviation.string,
                        current_abbreviation.count + 1,
                        current_abbreviation.index + 1
                    )
                )
                char = word[current_abbreviation.index]
                num_abbreviated = ""
                if current_abbreviation.count > 0:
                    num_abbreviated = str(current_abbreviation.count)
                stack.append(
                    Abbreviation(
                        current_abbreviation.string + num_abbreviated + char,
                        0,
                        current_abbreviation.index + 1
                    )
                )
        return abbreviations



# BFS Solution
# time complexity: sum(K * 2^K), for all 'K" from 1 to 'N'
# For a given word of size 'K' there are 2^K abbreviations and it takes
# O(K) time to create an abbreviation. This solution finds all abbreviations
# of all substrings of a word from size 1 to N, so then you need to sum up
# the amount of time it takes to find all of the abbreviations from size 1 to N
# space complexity: O(N * 2^N)
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        abbreviations = [""]
        if not word:
            abbreviations
        for character in word:
            new_abbreviations = []
            for old_abbreviation in abbreviations:
                new_abbreviations.append(old_abbreviation + character)
                if old_abbreviation and old_abbreviation[-1].isdigit():
                    new_number = str(int(old_abbreviation[-1]) + 1)
                    new_abbreviations.append(old_abbreviation[:-1] + new_number)
                else:
                    new_abbreviations.append(old_abbreviation + "1")
            abbreviations = new_abbreviations
        return abbreviations