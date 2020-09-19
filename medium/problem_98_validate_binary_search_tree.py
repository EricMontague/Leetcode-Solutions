
# Iterative Inorder Traversal Solution
#Time complexity: O(n), where 'n' is the number of nodes in the tree
# space complexity: O(h), where 'h' is the height of the tree
class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        lastNodeSeen = None
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                node = stack.pop()
                if lastNodeSeen and lastNodeSeen.val >= node.val:
                    return False
                lastNodeSeen = node
                root = node.right
            else:
                return True
  
  # Recursive DFS Solution
  #Time complexity: O(n), where 'n' is the number of nodes in the BST
# space complexity: O(h), where 'h' is the height of the tree
  class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root, float("inf"), float("-inf"))
    
    def _isValidBST(self, node, upperBound, lowerBound):
        if node is None:
            return True
        if node.val >= upperBound or node.val <= lowerBound:
            return False
        isLeftValid = self._isValidBST(node.left, node.val, lowerBound)
        isRightValid = self._isValidBST(node.right, upperBound, node.val)
        return isLeftValid and isRightValid
  
