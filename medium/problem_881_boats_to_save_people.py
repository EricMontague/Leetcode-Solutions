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


# Alternate Solution based on counting sort
# time complexity O(n + k), where 'n' is the number of people and 'k' is limit
# space complexity: O(k)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        groups = self.group_people_by_weight(people, limit)
        return self.count_num_boats(groups, limit)
        
    def group_people_by_weight(self, people, limit):
        groups = [0] * (limit + 1)
        for person_weight in people:
            groups[person_weight] += 1
        return groups
    
    def count_num_boats(self, groups, limit):
        num_boats = 0
        start = 0
        end = len(groups) - 1
        while start <= end:
            while start <= end and groups[start] <= 0:
                start += 1
            while start <= end and groups[end] <= 0:
                end -= 1
            if start > end:
                break
            if start + end <= limit:
                groups[start] -= 1
            groups[end] -= 1
            num_boats += 1
        return num_boats