"""This file contains my solutions to Leetcode problem 216."""


class Solution:
    def combinationSum3(self, combination_size: int, target: int) -> List[List[int]]:
        current_combination = []
        final_combinations = []
        max_choice = target - 1
        if target > 10:
            max_choice = 9
        self.generate_combinations(
            target, combination_size, max_choice, 1, current_combination, final_combinations
        )
        return final_combinations
    
    def generate_combinations(self, remaining, combo_size, max_choice, start, current, final):
        if remaining == 0 and len(current) == combo_size:
            final.append(current.copy())
        elif (
            remaining == 0 and len(current) < combo_size 
            or remaining > 0 and len(current) == combo_size
        ):
            return
        else:
            for num in range(start, max_choice + 1):
                if num > remaining:
                    break
                current.append(num)
                self.generate_combinations(
                    remaining - num, combo_size, max_choice, num + 1, current, final
                )
                current.pop()