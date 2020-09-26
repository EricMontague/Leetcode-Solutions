"""This file contains my solution to Leetcode problem 349: Intersection of Two Arrays."""

# time complexity: O(n + m), where 'n' is the number of integers in the first array,
# and 'm' is the number of integers in the second array
# space complexity: O(n), where 'n' is the number of integers in the first array

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        seen = self.buildBooleanHashTable(nums1)
        for num in nums2:
            if num in seen and not seen[num]:
                seen[num] = True
                intersection.append(num)
        return intersection
    
    def buildBooleanHashTable(self, nums):
        booleanHashTable = {num: False for num in nums}
        return booleanHashTable