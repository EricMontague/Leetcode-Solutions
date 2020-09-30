"""This file contains my solution to Leetcode problem 237:
Delete Node in a Linked List.
"""

# time and space complexity are O(1)
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next