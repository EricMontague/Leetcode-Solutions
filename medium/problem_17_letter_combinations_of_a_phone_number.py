"""This file contains my solution for Leetcode problem 17: Letter Combinations
of a Phone Number.
"""


# time complexity: O(3^N x 4^M), where 'N' is the number of digits in the input
# that maps to 3 letters and 'M' is the number of digits in the input that maps
# to 4 letters.

# Note: N + M is the total number of digits in the input

# space complexity: O(3^N x 4 ^M) since you have to keep 3 ^ N x 4 ^ M solutions
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        self.generate_combinations(digits, 0, [], combinations)
        return combinations
    
    def generate_combinations(self, digits, index, combination, combinations):
        if index == len(digits):
            combinations.append("".join(combination))
        else:
            for character in self.get_characters(digits[index]):
                combination.append(character)
                self.generate_combinations(
                    digits,
                    index + 1,
                    combination,
                    combinations
                )
                combination.pop()
    
    def get_characters(self, digit):
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        return mapping[digit]