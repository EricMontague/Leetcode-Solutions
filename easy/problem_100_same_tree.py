"""This file contains my solutions to Leetcode problem 100: Same Tree."""

# time complexity: O(n + m), where 'n' is the number of nodes in the first tree and
# 'm' is the number of nodes in the second tree
# space complexity: O(min(n, m))

# Recursive Solution
class Solution:
    def isSameTree(self, original: TreeNode, clone: TreeNode) -> bool:
        if not original and not clone:
            return True
        if not original or not clone:
            return False
        if original.val != clone.val:
            return False
        isSameLeftSubtree = self.isSameTree(original.left, clone.left)
        if not isSameLeftSubtree:
            return False
        isSameRightSubtree = self.isSameTree(original.right, clone.right)
        return isSameRightSubtree


# Iterative Solution (Same time and space complexity as above)
class Solution:
    def isSameTree(self, original: TreeNode, clone: TreeNode) -> bool:
        stack = [(original, clone)]
        while stack:
            originalNode, cloneNode = stack.pop()
            if not self.isSameNode(originalNode, cloneNode):
                return False
            if originalNode and cloneNode:
                stack.append((originalNode.right, cloneNode.right))
                stack.append((originalNode.left, cloneNode.left))
        return True
    
    def isSameNode(self, originalNode, cloneNode):
        if not originalNode and not cloneNode:
            return True
        if not originalNode or not cloneNode:
            return False
        if originalNode.val != cloneNode.val:
            return False
        return True