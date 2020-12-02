"""This file contains my solutions to Leetcode problem 784."""



# time complexity: O(N * 2^N), where 'n' is the length of the string
# space complexity: O(N * 2^N)
class Solution:
    def letterCasePermutation(self, string: str) -> List[str]:
        if not string:
            return [""]
        permutations = []
        current_permutation = []
        self.generate_permutations(
            string,
            0,
            current_permutation,
            permutations
        )
        return permutations
    
    def generate_permutations(self, string, index, current_permutation, permutations):
        if index == len(string):
            permutations.append("".join(current_permutation))
        else:
            for character in {string[index].lower(), string[index].upper()}:
                current_permutation.append(character)
                self.generate_permutations(
                    string,
                    index + 1,
                    current_permutation,
                    permutations
                )
                current_permutation.pop()
    

# time complexity: O(N * 2^N), where 'n' is the length of the string
# space complexity: O(N * 2^N)
class Solution:
    def letterCasePermutation(self, string: str) -> List[str]:
        combinations = [""]
        for character in string:
            new_combinations = []
            for old_combination in combinations:
                if character.isdigit():
                    new_combination = old_combination + character
                    new_combinations.append(new_combination)
                else:
                    new_combination_lower = old_combination + character.lower()
                    new_combination_upper = old_combination + character.upper()
                    new_combinations.append(new_combination_lower)
                    new_combinations.append(new_combination_upper)
            combinations = new_combinations
        return combinations