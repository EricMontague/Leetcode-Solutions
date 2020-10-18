"""This file contains my solutions to Leetcode problem 875: Koko Eating Banans."""


# time complexity: O(nlogk), where 'n' is the number of integers in piles,
# and 'k' is the range from 1 to the largest integer in piles

# space complexity: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            eating_speed = low + (high - low) // 2
            time_elapsed = self.count_time_eat_at_speed(piles, eating_speed)
            if time_elapsed <= hours:
                high = eating_speed
            else:
                low = eating_speed + 1
        return low

    def count_time_eat_at_speed(self, piles, eating_speed):
        hours = 0
        for pile in piles:
            hours += (pile - 1) // eating_speed + 1
        return hours
