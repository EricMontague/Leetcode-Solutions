"""This file contains my solutions to Leetcode problem 199: Binary Tree Right Side View."""


# BFS Solution
# time complexity: O(n), where 'n' is the number of nodes in the binary tree
# space complexity: O(n)
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_side_view = []
        if not root:
            return right_side_view
        previous_node = root
        previous_level = 0
        queue = deque([(previous_node, previous_level)])
        while queue:
            current_node, current_level = queue.popleft()
            if current_level != previous_level:
                right_side_view.append(previous_node.val)
                previous_level = current_level
            previous_node = current_node
            if current_node.left:
                queue.append((current_node.left, current_level + 1))
            if current_node.right:
                queue.append((current_node.right, current_level + 1))
        right_side_view.append(previous_node.val)
        return right_side_view


# DFS Solution
# time complexity: O(n)
# space complexity: O(h), where 'h' is the height of the binary tree
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        tree_levels = {}
        if not root:
            return tree_levels.values()
        stack = [(root, 0)]
        while stack:
            current_node, current_level = stack.pop()
            
            tree_levels[current_level] = current_node.val
            if current_node.right:
                stack.append((current_node.right, current_level + 1))
            if current_node.left:
                stack.append((current_node.left, current_level + 1))
        return tree_levels.values()
        