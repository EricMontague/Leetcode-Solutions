"""This is my solution for problem 543."""

#Overall time complexity: O(n), where n is the number of nodes in the tree
#Overall space complexity: O(h), where h is the height of the tree.
class Solution:
    
    def __init__(self):
        self.maxSubtreeHeight = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.findTreeHeight(root)
        return self.maxSubtreeHeight
    
    def findTreeHeight(self, root):
        if root is not None:
            leftSubtreeHeight = self.findTreeHeight(root.left)
            rightSubtreeHeight = self.findTreeHeight(root.right)
            self.maxSubtreeHeight = max(leftSubtreeHeight + rightSubtreeHeight, self.maxSubtreeHeight)
            return 1 + max(leftSubtreeHeight, rightSubtreeHeight)
        return 0
    