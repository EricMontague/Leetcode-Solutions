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



# Solution to a theoretical follow-up with sorted array
# The below solution assumes that both input arrays are sorted
# time complexity: O(max(n, m))
# space complexity: O(1)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
            while left > 0 and left < nums1Length and nums1[left - 1] == nums1[left]:
                left += 1
            while right > 0 and right < nums2Length and nums2[right - 1] == nums2[right]:
                right += 1
        return intersection