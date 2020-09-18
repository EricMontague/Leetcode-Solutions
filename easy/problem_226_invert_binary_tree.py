"""This file contains my solutions to Leetcode problrm 226: Invert Binary Tree."""


# BFS Solution
# Overall time complexity is O(n), where n is the number of nodes in the tree
# Overall space complexity is O(n), where n is the number of nodes in the tree
from queue import Queue


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = Queue()
        queue.put_nowait(root)
        while not queue.empty():
            node = queue.get_nowait()
            self.swapChildren(node)
            if node.left:
                queue.put_nowait(node.left)
            if node.right:
                queue.put_nowait(node.right)
        return root

    def swapChildren(self, node):
        node.left, node.right = node.right, node.left


# Recursive DFS Solution
# Overall time complexity is O(n), where n is the number of nodes in the tree
# Overall space complexity is O(n), where n is the number of nodes in the tree
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        leftChild = root.left
        rightChild = root.right
        root.left = self.invertTree(rightChild)
        root.right = self.invertTree(leftChild)
        return root


# Iterative DFS Solution
# Overall time complexity is O(n), where n is the number of nodes in the tree
# Overall space complexity is O(n), where n is the number of nodes in the tree
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return root
