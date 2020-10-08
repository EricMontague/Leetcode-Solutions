"""This file contains my solutions to leetcode problem 881: Boats to Save People."""


# time complexity: O(nlogn) , where 'n' is the number of people
# space complexity: O(n)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = 0
        people.sort()
        start = 0
        end = len(people) - 1
        while start <= end:
            total_weight = people[start] + people[end]
            if total_weight <= limit:
                start += 1
            end -= 1
            num_boats += 1
        return num_boats