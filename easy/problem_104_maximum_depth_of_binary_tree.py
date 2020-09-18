"""These are my solutions to problem 104: Maximum Depth of Binary Tree."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Overall time complexity is O(n), where n is the number of nodes in the tree
# Over space complexity is O(h), where h is the height of the binary tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Overall time complexity is O(n), where n is the number of nodes in the tree
# Over space complexity is O(h), where h is the height of the binary tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        if root is None:
            return max_depth
        stack = [(root, 1)]
        while stack:
            root, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            if root.right is not None:
                stack.append((root.right, depth + 1))
            if root.left is not None:
                stack.append((root.left, depth + 1))
        return max_depth


# Overall time complexity is O(n), where n is the number of nodes in the tree
# Over space complexity is O(h), where h is the height of the binary tree
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maxDepth = 0
        if not root:
            return maxDepth
        queue = deque()
        queue.append((root, maxDepth + 1))

        while queue:
            node, depth = queue.popleft()
            maxDepth = max(depth, maxDepth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return maxDepth
