"""This file contains my solution for Leetcode problem 173: Binary Search Tree Iterator."""


# time complexities
# hasNext() - O(1)
# next() - Amortized constants time

# space complexity: O(h), where 'h' is the height of the tree
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftMostInorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        topNode = self.stack.pop()
        self._leftMostInorder(topNode.right)
        return topNode.val
            
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
    
    def _leftMostInorder(self, root):
        current = root
        while current:
            self.stack.append(current)
            current = current.left

