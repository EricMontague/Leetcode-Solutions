"""This file contains my solution to Leetcode problem 142: Linked List Cycle II."""


# time complexity: O(n), where 'n' is the number of nodes in the linked list
# space complexity: O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        meetingPoint = self.findMeetingPoint(head)
        if not meetingPoint:
            return meetingPoint
        return self.findStartOfCycle(head, meetingPoint)
    
    def findMeetingPoint(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    
    def findStartOfCycle(self, head, meetingPoint):
        first = head
        second = meetingPoint
        while first != second:
            first = first.next
            second = second.next
        return first