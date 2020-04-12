"""This is my solution to Leetcode problem 228."""


#Overall time complexity: O(n), where "n" is the number of integers in nums
#Overall space complexity: O(n), where "n" is the number of integers in nums
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        summaryRanges = []
        while start < len(nums):
            end = start
            while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end += 1
            self.formatRange(nums, start, end, summaryRanges)
            start = end + 1
        return summaryRanges
    
    def formatRange(self, nums, start, end, summaryRanges):
        if start == end:
            summaryRanges.append(str(nums[end]))
        else:
            summaryRanges.append(str(nums[start]) + "->" + str(nums[end]))


#Intuition:
#Loop through the list keeping track of the starting and ending indices of a range. Once
#You have both, you can format the range properly and insert it into the output list.

#First assume the starting range is at index 0. Set end equal to start because initially,
#a number can be both the start and end of a range. Increment the variable end 
#(simulating moving a pointer forward in the list) as long as the next number in the list is
#one greater than the current number at index "end" and as long as you are not at the end of the list.

#Finally, once the loop exits, you know that "end" is equal to the index of the last number in the range
#and you can call your helper method to format the range. Set start = end + 1 so that you can begin searching
#for a new range on the next loop around.
