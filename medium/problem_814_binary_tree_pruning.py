"""This script contains my solution to Leetcode problem 814: Binary Tree Pruning."""


# Overall time complexity: O(n) where "n" is the number of nodes in the tree
# Overall space complexity: O(h) where "h" is the height of the tree
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root
    
        