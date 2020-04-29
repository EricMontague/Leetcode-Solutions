"""This script contains my solutions to Leetcode problem 1379."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#BFS
#Overall time complexity: O(n)
#Overall space complexity: O(n)
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        maxDepth = 0
        leavesSum = 0
        if root is None:
            return leavesSum
        queue = deque()
        queue.append((root, maxDepth))
        while queue:
            node, depth = queue.popleft()
            if depth > maxDepth:
                maxDepth = depth
                leavesSum = 0    
            leavesSum += node.val
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))
        return leavesSum


#Recursive DFS
#Overall time complexity: O(n)
#Overall space complexity: O(h)
class Solution:
    maxDepth = 0
    leavesSum = 0
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.inorderTraversal(root, depth=0)
        return self.leavesSum
    
    def inorderTraversal(self, node, depth):
        if node is not None:
            if depth == self.maxDepth:
                self.leavesSum += node.val
            elif depth > self.maxDepth:
                self.maxDepth = depth
                self.leavesSum = node.val
            self.inorderTraversal(node.left, depth + 1)
            self.inorderTraversal(node.right, depth + 1)
                

#Iterative DFS
#Overall time complexity: O(n)
#Overall space complexity: O(h)
class Solution:
     
    def deepestLeavesSum(self, root: TreeNode) -> int:
        maxDepth = 0
        leavesSum = 0
        if root is None:
            return leavesSum
        stack = [(root, maxDepth)]
        while stack:
            node, depth = stack.pop()
            if depth == maxDepth:
                maxDepth = depth
                leavesSum += node.val
            elif depth > maxDepth:
                maxDepth = depth
                leavesSum = node.val
            if node.right is not None:
                stack.append((node.right, depth + 1))
            if node.left is not None:
                stack.append((node.left, depth + 1))
        return leavesSum

        