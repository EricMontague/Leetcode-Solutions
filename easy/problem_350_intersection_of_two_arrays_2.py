"""This file contains my solution to Leetcode problem 349: Intersection of Two Arrays."""


# time complexity: O(n + m), where 'n' is the number of integers in the first array,
# and 'm' is the number of integers in the second array
# space complexity: O(min(n, m))
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            counter = Counter(nums1)
            return self.makeIntersection(nums2, counter)
        else:
            counter = Counter(nums2)
            return self.makeIntersection(nums1, counter)
    
    def makeIntersection(self, nums, counter):
        intersection = []
        for num in nums:
            if num in counter and counter[num] > 0:
                intersection.append(num)
                counter[num] -= 1
        return intersection