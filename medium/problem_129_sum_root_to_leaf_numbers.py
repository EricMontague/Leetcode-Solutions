"""This file contains my solutions to Leetcode problem 129:
Sum Root to leaf numbers
"""


# time complexity: O(n), where 'n' is the number of nodes
# space complexity: O(h), where 'h' is the height of the tree

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.sum_paths(root, 0)
    
    def sum_paths(self, node, number):
        if node is None:
            return 0
        new_number = number * 10 + node.val
        if node.left is None and node.right is None:
            return new_number
        return (
            self.sum_paths(node.left, new_number)
            + self.sum_paths(node.right, new_number)
        )


# time complexity: O(n), where 'n' is the number of nodes
# space complexity: O(h), where 'h' is the height of the tree
class Solution:
    
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        sum_ = 0
        stack = [(root, 0)]
        while stack:
            node, number = stack.pop()
            new_number = number * 10 + node.val
            if node.left is None and node.right is None:
                sum_ += new_number
            if node.right is not None:
                stack.append((node.right, new_number))
            if node.left is not None:
                stack.append((node.left, new_number))
        return sum_