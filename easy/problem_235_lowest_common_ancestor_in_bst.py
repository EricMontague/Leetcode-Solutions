"""This file contains my solution to Leetcode problem 235:
Lowest Common Ancestor in BST."""


# time complexity: O(h), where 'h' is the height of the bst
# space complexity: O(h), where 'h' is the height of the bst
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root