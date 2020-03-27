"""This is my solution to problem 1217."""


#Overall time complexity is O(n), where n is the number of chips
#Overall space complexity is O(1)
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        if not chips:
            return 0
        num_even_positions = 0
        num_odd_positions = 0
        for chip in chips:
            if chip % 2 == 0:
                num_even_positions += 1
            else:
                num_odd_positions +=1
        return min(num_even_positions, num_odd_positions)
