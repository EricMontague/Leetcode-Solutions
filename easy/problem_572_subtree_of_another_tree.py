"""This file contains my solution to Leetcode problem 572: Subtree of Another Tree."""


# time complexity: O(nm), where 'n' is the number of nodes in the original tree
# and 'm' is the number of nodes in the possible subtree
# space complexity: O(n + m)
class Solution:
    def isSubtree(self, original: TreeNode, subtree: TreeNode) -> bool:
        originalNodes = self.convertTreeToArray(original)
        subtreeNodes = self.convertTreeToArray(subtree)
        return self.isSubArray(originalNodes, subtreeNodes)
    
    def convertTreeToArray(self, root):
        nodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                nodes.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                nodes.append(node)
        return nodes
    
    def isSubArray(self, originalArray, subArray):
        originalLength = len(originalArray)
        subArrayLength = len(subArray)
        for index in range(originalLength - subArrayLength + 1):
            if originalArray[index: index + subArrayLength] == subArray:
                return True
        return False


# Recursive Solution
# time complexity: O(nm), where 'n' is the number of nodes in the original tree
# and 'm' is the number of nodes in the possible subtree
# space complexity: O(max(n, n))
class Solution2:
    def isSubtree(self, original: TreeNode, subtree: TreeNode) -> bool:
        return self.validateSubtree(original, subtree)
    
    def validateSubtree(self, original, subtree):
        if not original:
            return False
        if original.val != subtree.val:
            isLeftSubtree = self.validateSubtree(original.left, subtree)
            isRightSubtree = self.validateSubtree(original.right, subtree)
            return isLeftSubtree or isRightSubtree
        else:
            sameSubtree = self.isSameTree(original, subtree)
            if sameSubtree:
                return True
            isLeftSubtree = self.validateSubtree(original.left, subtree)
            isRightSubtree = self.validateSubtree(original.right, subtree)
            return isLeftSubtree or isRightSubtree
        
    
    def isSameTree(self, original, clone):
        if not original and not clone:
            return True
        if not original or not clone:
            return False
        if original.val != clone.val:
            return False
        return self.isSameTree(original.left, clone.left) and self.isSameTree(original.right, clone.right)