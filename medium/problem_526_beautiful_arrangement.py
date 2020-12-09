"""This file contains my solutions for problem 526."""
class Solution:
    def countArrangement(self, num_arrangements: int) -> int:
        picked = set()
        return self.compute_num_arrangements(
            num_arrangements, 1, picked
        )
    
    def compute_num_arrangements(self, num_arrangements, position, picked):
        if position > num_arrangements:
            return 1
        total = 0
        for num in range(1, num_arrangements + 1):
            if num not in picked:
                if (
                    position % num == 0 
                    or num % position == 0
                ):
                    picked.add(num)
                    total += self.compute_num_arrangements(
                        num_arrangements,
                        position + 1,
                        picked
                    )
                    picked.remove(num)
        return total