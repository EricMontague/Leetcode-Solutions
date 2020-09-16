"""This file contains my solutions to leetcode problem 1008: Construct Binary Search Tree 
from Preorder Traversal.
"""


# Recursive solution

# time complexity: O(n), where 'n' is the number of nodes in the bst
# space complexity: O(n), where 'n' is the number of nodes in the bst


class Solution:
    def __init__(self):
        self.currentNodeIdx = 0

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        return self.constructBST(TreeNode(float("inf")), preorder)

    def constructBST(self, leftSubtreeRoot, preorderList):
        if (
            self.currentNodeIdx == len(preorderList)
            or preorderList[self.currentNodeIdx] > leftSubtreeRoot.val
        ):
            return None
        node = TreeNode(preorderList[self.currentNodeIdx])
        self.currentNodeIdx += 1
        node.left = self.constructBST(node, preorderList)
        node.right = self.constructBST(leftSubtreeRoot, preorderList)
        return node


# Iterative solution

# time complexity: O(n), where 'n' is the number of nodes in the bst
# space complexity: O(n), where 'n' is the number of nodes in the bst


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [(root, TreeNode(float("inf")))]
        currentNodeIdx = 1
        while currentNodeIdx < len(preorder):
            parent, leftSubtreeRoot = stack[-1]
            if preorder[currentNodeIdx] < parent.val:
                parent.left = TreeNode(preorder[currentNodeIdx])
                stack.append((parent.left, parent))
                currentNodeIdx += 1
            else:
                if preorder[currentNodeIdx] < leftSubtreeRoot.val:
                    parent.right = TreeNode(preorder[currentNodeIdx])
                    stack.append((parent.right, leftSubtreeRoot))
                    currentNodeIdx += 1
                else:
                    stack.pop()
        return root
