"""This script contains my solution to Leetcode problem 1305."""


#Overall time complexity: O(n + m), where 'n' is the number of nodes in the first tree
#and 'm' is the number of nodes in the second tree
#Overall space complexity: O(n + m)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        leftNodes = []
        rightNodes = []
        self.inOrderTraversal(root1, leftNodes)
        self.inOrderTraversal(root2, rightNodes)
        return self.merge(leftNodes, rightNodes)
    
    def inOrderTraversal(self, node, nodes):
        if node is None:
            return
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            nodes.append(node.val)
            node = node.right
            
    def merge(self, leftNodes, rightNodes):
        merged = []
        i = 0
        j = 0
        while i < len(leftNodes) and j < len(rightNodes):
            if leftNodes[i] <= rightNodes[j]:
                merged.append(leftNodes[i])
                i += 1
            else:
                merged.append(rightNodes[j])
                j += 1
        
        while i < len(leftNodes):
            merged.append(leftNodes[i])
            i += 1
        
        while j < len(rightNodes):
            merged.append(rightNodes[j])
            j += 1
        return merged


#Intuition: Perform and inorder traversal on both trees. Each time you visit a node during
#the traversal, add it to a list. Since traversing a BST using an inorder traversal visits
#all of the nodes in sorted order, you will then have two sorted lists of values.
#You can then merge both sorted lists into one final sorted list in linear time, similar
#to how merge sort does

