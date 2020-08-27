"""This file contains my solutions for Leetcode problem 239: Sliding Window Maximum."""


# Solution 1
# time complexity: O(nlogn), where 'n' is the number of integers in nums
# space complexity: O(n), where 'n' is the number of integers in nums
class TreeNode:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def search(self, value):
        if not self.root:
            return self.root
        return self._findNode(self.root, value)
    
    def _findNode(self, node, value):
        if node is None:
            return node
        if node.value == value:
            return node
        elif value < node.value:
            return self._findNode(node.left, value)
        else:
            return self._findNode(node.right, value)
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root = self._insertNode(self.root, value)
    
    def _insertNode(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insertNode(node.left, value)
        else:
            node.right = self._insertNode(node.right, value)
        return node
    
    def delete(self, value):
        targetNode = self.search(value)
        if not targetNode:
            raise ValueError("Node not in tree")
        self.root = self._deleteNode(self.root, value)
    
    def _deleteNode(self, node, value):
        if value < node.value:
            node.left = self._deleteNode(node.left, value)
        elif value > node.value:
            node.right = self._deleteNode(node.right, value)
        else:
            # Case 1: No children
            if not node.left and not node.right:
                node = None
            # Case 2: One child
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else: # Case 3: Two children
                maxNode = self.findMax(node.left)
                node.value = maxNode.value
                node.left = self._deleteNode(node.left, maxNode.value)
        return node
    
    def findMax(self, node):
        if not node or not node.right:
            return node
        return self.findMax(node.right)
            

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        tree = self.buildTree(nums, k)
        for index in range(k, len(nums)):
            maxNode = tree.findMax(tree.root)
            maxElements.append(maxNode.value)
            tree.delete(nums[index - k])
            tree.insert(nums[index])
        lastMaxNode = tree.findMax(tree.root)
        maxElements.append(lastMaxNode.value)
        return maxElements
    
    def buildTree(self, nums, k):
        tree = BinarySearchTree()
        for index in range(k):
            tree.insert(nums[index])
        return tree