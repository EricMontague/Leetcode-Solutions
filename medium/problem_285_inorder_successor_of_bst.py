"""This file contains my solutions to Leetcode problem 285: Inorder Successor of BST."""


# time complexity: O(h), where 'h' is the height of the BST
# space complexity: O(h)
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        return self.find_inorder_successor(root, None, p)
    
    def find_inorder_successor(self, current, ancestor, target):
        if current is None:
            return None
        if current == target:
            if current.right is not None:
                return self.find_min(current.right)
            return ancestor
        if target.val < current.val:
            return self.find_inorder_successor(current.left, current, target)
        return self.find_inorder_successor(current.right, ancestor, target)
    
    def find_min(self, root):
        if root is None:
            return None
        if root.left is None:
            return root
        return self.find_min(root.left)


# time complexity: O(h), where 'h' is the height of the BST
# space complexity: O(1)
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', target: 'TreeNode') -> 'TreeNode':
        ancestor = None
        current = root
        while current is not None:
            if current == target:
                if current.right is not None:
                    return self.find_min(current.right)
                return ancestor
            if target.val < current.val:
                ancestor = current
                current = current.left
            else:
                current = current.right
        return None
    
    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current
                