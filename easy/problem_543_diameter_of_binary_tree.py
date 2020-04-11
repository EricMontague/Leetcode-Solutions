"""This is my solution for problem 543."""

#Overall time complexity: O(n), where n is the number of nodes in the tree
#Overall space complexity: O(h), where h is the height of the tree.
class Solution:
    
    def __init__(self):
        self.maxSubtreeDiameter = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.findTreeHeight(root)
        return self.maxSubtreeDiameter
    
    def findTreeHeight(self, root):
        if root is not None:
            leftSubtreeHeight = self.findTreeHeight(root.left)
            rightSubtreeHeight = self.findTreeHeight(root.right)
            self.maxSubtreeDiameter = max(leftSubtreeHeight + rightSubtreeHeight, self.maxSubtreeDiameter)
            return 1 + max(leftSubtreeHeight, rightSubtreeHeight)
        return 0

#Intuition
#This problem really boils down to finding the subtree with the maximum diameter within
#the tree. The diameter of a subtree can be expresssed as the height of the left subtree
#plus the height of the right subtree, where a leaf node's height is considered to be 1 and
# null pointers are considered to have a height of 0. 
# After getting these two values you can compare the diameter of the current subtree to the known maximum subtree diameter.
#After recursing through all "n" nodes, you will eventually find the subtree with the
#maximum diameter
