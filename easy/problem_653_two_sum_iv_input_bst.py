"""This file contains my solutions to Leetcode problem 653: Two Tum IV - Input is a BST."""


# time complexity: O(n), where 'n' is the number of nodes in the BST
# space complexity: O(n), where 'n' is the number of nodes in the BST
from collections import deque
class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        complementSet = set()

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if target - node.val in complementSet:
                return True
            complementSet.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return False
        

# time complexity: O(n), where 'n' is the number of nodes in the BST
# space complexity: O(n), where 'n' is the number of nodes in the BST
class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        complementSet = set()
        return self.canMakeSum(root, complementSet, target)

    def canMakeSum(self, node, complementSet, target):
            if not node:
                return False
            if target - node.val in complementSet:
                return True
            complementSet.add(node.val)
            left = self.canMakeSum(node.left, complementSet, target)
            right = self.canMakeSum(node.right, complementSet, target)
            return left or right

