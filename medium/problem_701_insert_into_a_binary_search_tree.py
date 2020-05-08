"""This script contains my solution to Leetcode problem 701: Insert into a
Binary Search Tree.
"""


#Overall time complexity: O(h), where "h" is the height of the tree. If the BST
#is balanced, then this will be O(logn), but if it is skewed, it will be O(n)

#Overall space complexity: O(h). Same explanation as above

#Note: The space complexity can be improved to O(1) if implemented iteratively
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return self._insert(root, val)
        
    def _insert(self, root, val):
        if root is None:
            return TreeNode(val=val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


        