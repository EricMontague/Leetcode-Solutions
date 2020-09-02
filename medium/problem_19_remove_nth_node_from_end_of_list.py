"""This file contains my solution to Leetcode problem 19:
Remove Nth Node from End of List.
"""

# time complexity: O(n), where 'n' is the number of nodes in the linked list
# space complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        sentinel = ListNode(-1, head)
        previous = sentinel
        current = head
        fast = self.traverseNNodes(head, n - 1)
        while fast.next is not None:
            previous = previous.next
            current = current.next
            fast = fast.next
        previous.next = current.next
        return sentinel.next
    
    def traverseNNodes(self, head, n):
        current = head
        for node in range(n):
            current = current.next
        return current