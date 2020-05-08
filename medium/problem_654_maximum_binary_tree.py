"""This script contains my solution to Leetcode problem 654: Maximum Binary Tree."""


#Overall time complexity: O(n^2) in the worst case, O(nlogn) in the average case.
#Overall space complexity: O(n) in the worst case, Ol(logn) in the average case
#The intuition behind the time and space complexities is similar to quicksort
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        start = 0
        end = len(nums) - 1
        return self.constructTree(start, end, nums)
    
    def constructTree(self, start, end, nums):
        if start > end:
            return None
        maxIndex = self.getMaxIndex(start, end, nums)
        node = TreeNode(val=nums[maxIndex])
        node.left = self.constructTree(start, maxIndex - 1, nums)
        node.right = self.constructTree(maxIndex + 1, end, nums)
        return node
    
    def getMaxIndex(self, start, end, nums):
        maxIndex = start
        for index in range(start, end + 1):
            if nums[index] > nums[maxIndex]:
                maxIndex = index
        return maxIndex

