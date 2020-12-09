"""This file contains my solutions for Leetcode problem 897: 
Increasing Order Search Tree.

"""

# Recursive Solution
# time complexity: O(n), where 'n' is the number of nodes
# space complexity: O(h), where 'h' is the height of the tree
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        temp = TreeNode(None)
        self.last_node = temp
        self.reassign_pointers(root)
        return temp.right
    
    def reassign_pointers(self, current_node):
        if current_node is not None:
            self.reassign_pointers(current_node.left)
            current_node.left = None
            self.last_node.right = current_node
            self.last_node = current_node
            self.reassign_pointers(current_node.right)


# Iterative solution
# time complexity: O(n), where 'n' is the number of nodes
# space complexity: O(h), where 'h' is the height of the tree
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        temp = TreeNode(None)
        last_node = temp
        stack = []
        while stack or root:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                node.left = None
                last_node.right = node
                last_node = node
                root = node.right
        return temp.right