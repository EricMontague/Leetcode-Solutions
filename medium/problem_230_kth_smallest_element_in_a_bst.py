"""This file contains my solution to Leetcode problem 230:
Kth Smallest Element in a BST."""

# time complexity: O(h + k), where 'h' is the height of the BST and 'k' is the parameter k
# space complexity O(h), where 'h' is the height of the BST


class Solution:
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        lastK = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                node = stack.pop()
                lastK += 1
                if lastK == k:
                    return node.val
                root = node.right
        
    