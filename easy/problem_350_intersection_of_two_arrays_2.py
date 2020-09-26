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


# Solution to follow-up with sorted array
# The below solution assumes that both input arrays are sorted
# time complexity: O(max(n, m))
# space complexity: O(1)


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        left = 0
        right = 0
        nums1Length = len(nums1)
        nums2Length = len(nums2)
        while left < nums1Length and right < nums2Length:
            if nums1[left] == nums2[right]:
                intersection.append(nums1[left])
                left += 1
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return intersection