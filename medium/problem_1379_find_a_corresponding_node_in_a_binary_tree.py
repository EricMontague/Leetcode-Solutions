"""This script contains my solutions to Leetcode problem 1379:  
Find a Corresponding Node of a Binary Tree in a Clone of That Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Depth-First Search
#Overall time complexity: O(n), where "n" is the number of nodes in the tree
#Overall space complexity: O(h), where "h" is the height of the binary tree
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack:
            original, cloned = stack.pop()
            if original == target:
                return cloned
            if original.left is not None:
                stack.append((original.left, cloned.left))
            if original.right is not None:
                stack.append((original.right, cloned.right))
        return None
    

#Depth-First Search
#Overall time complexity: O(n), where "n" is the number of nodes in the tree
#Overall space complexity: O(h), where "h" is the height of the binary tree
class Solution:
    copy = None
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.preorderTraversal(original, cloned, target)
        return self.copy
    
    def preorderTraversal(self, original, cloned, target):
        if original is not None and cloned is not None:
            if original == target:
                self.copy = cloned
            self.preorderTraversal(original.left, cloned.left, target)
            self.preorderTraversal(original.right, cloned.right, target)
    

#Breadth-First Search
#Overall time complexity: O(n), where "n" is the number of nodes in the tree
#Overall space complexity: O(n), where "n" is the number of nodes in the tree
from collections import deque
class Solution:
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:    
        queue = deque()
        queue.append((original, cloned))
        while queue:
            original, cloned = queue.popleft()
            if original == target:
                return cloned
            if original.left is not None:
                queue.append((original.left, cloned.left))
            if original.right is not None:
                queue.append((original.right, cloned.right))
        return None


#Intuition:
#The general intuition in all of the solutions is to traverse both trees at the
#same time. At each point in the traversal, check whether the node you're at in the original
#tree is the same as the target node. If it is, this means that the node that you're at
#in the cloned tree is the copy of the target.
   
        