"""This is my solution to Leetcode problem 450."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Overall time complexity: O(h)
#Overall space complexity: O(h)
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                min_node = self.getMinNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root
    
    def getMinNode(self, root):
        if root.left is None:
            return root
        return self.getMinNode(root.left)
    
    