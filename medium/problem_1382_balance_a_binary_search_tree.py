"""This file contains my solutions to Leetcode problem 1382: Balance a BST."""

# time complexity: O(n), where 'n' is the number of nodes in the tree
# space complexity: O(n)

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_nodes = self.convert_bst_to_sorted_array(root)
        return self.build_bst_from_sorted_array(sorted_nodes, 0, len(sorted_nodes) - 1)
    
    def convert_bst_to_sorted_array(self, root):
        sorted_nodes = []
        if not root:
            return sorted_nodes
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                node = stack.pop()
                sorted_nodes.append(node)
                root = node.right
        return sorted_nodes
    
    def build_bst_from_sorted_array(self, sorted_nodes, low, high):
        if low > high:
            return None
        mid = low + (high - low) //2
        new_node = sorted_nodes[mid]
        new_node.left = self.build_bst_from_sorted_array(sorted_nodes, low, mid - 1)
        new_node.right = self.build_bst_from_sorted_array(sorted_nodes, mid + 1, high)
        return new_node