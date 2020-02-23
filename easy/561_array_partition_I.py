"""Solution to problem 561 on Leetcode: Array Partition I."""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = 0
        for index in range(0, len(nums), 2):
            pair_sum += min(nums[index], nums[index + 1])
        return pair_sum


#Time complexity is O(n + nlogn), but since we only care about
#the fasting growing terms, the overall time complexity is O(nlogn)

#Space complexity is O(1) because regardless of how larger the input
#size gets, we will not use any extra space.





