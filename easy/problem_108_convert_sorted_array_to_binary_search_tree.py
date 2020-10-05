"""This file contains my solutions to Leetcode problem 108: Convert Sorted Array to Binary Search Tree."""


# time complexity: O(n), where 'n' is the number of integers in nums
# space complexity: O(n), where 'n' is the number of integers in nums

# although if you don't count the output as space, then the space complexity will be O(log n)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build_bst_from_sorted_array(nums, 0, len(nums) - 1)
        
    
    def build_bst_from_sorted_array(self, nums, low, high):
        if low > high:
            return None
        mid = low + (high - low) // 2
        new_node = TreeNode(nums[mid])
        new_node.left = self.build_bst_from_sorted_array(
            nums, low, mid - 1
        )
        new_node.right = self.build_bst_from_sorted_array(
            nums, mid + 1, high
        )
        return new_node