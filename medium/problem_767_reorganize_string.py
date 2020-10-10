"""This file contains my solutions to Leetcode problem 767: Reorganize String."""



class Solution:
    def reorganizeString(self, string: str) -> str:
        return self.reorganize(string, "")
    
    def reorganize(self, remaining_chars, prefix):
        if remaining_chars == "":
            return prefix
        for index, char in enumerate(remaining_chars):
            if not prefix or char != prefix[-1]:
                reorganized_string = self.reorganize(
                    remaining_chars[0: index] + remaining_chars[index + 1:],
                    prefix + remaining_chars[index]
                )
                if reorganized_string != "":
                    return reorganized_string
        return ""