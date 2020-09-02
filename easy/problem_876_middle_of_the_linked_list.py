"""This file contains my solution to Leetcode problem 876: Middle of the Linked List."""


# time complexity: O(n), where 'n' is the number of nodes in the linked list
# space complexity: O(1)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow