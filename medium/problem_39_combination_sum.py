"""This file contains my solutions for Leetcode problem 39: Combination Sum."""



# time complexity: O(2 ^n + k), where 'n' is the length of candidates, and 'k' is the length
# of all combinations
# space complexity: O(m + k), where 'm' is the number of combinations and 'k'
# is the sum of the lengths of all combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combos = []
        self.make_combos(candidates, target, len(candidates) - 1, [])
        return self.combos
    
    def make_combos(self, candidates, target, index, combo):
        if index == -1:
            return
        if target == 0:
            self.combos.append(combo[:])
            return
        if candidates[index] <= target:
            combo.append(candidates[index])
            self.make_combos(candidates, target - candidates[index], index, combo)
            combo.pop()
        self.make_combos(candidates, target, index - 1, combo)