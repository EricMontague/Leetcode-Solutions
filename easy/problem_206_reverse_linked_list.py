"""This script contains my solutions to Leetcode problem 206: Reverse Linked List."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Overall time complexity: O(n), where n is the number of nodes in the linked list
#Overall space complexity: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current is not None:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        head = previous
        return head




#Overall time complexity: O(n), where n is the number of nodes in the linked list
#Overall space complexity: O(n), where n is the number of nodes in the linked list
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        stack = []
        self.pushNodesToStack(head, stack)
        head = self.popNodesFromStack(stack)
        return head
    
    def pushNodesToStack(self, head, stack):
        current = head
        while current is not None:
            stack.append(current)
            current = current.next
    
    def popNodesFromStack(self, stack):
        head = stack.pop()
        current = head
        while stack:
            node = stack.pop()
            current.next = node
            current = node
        current.next = None
        return head


#Overall time complexity: O(n), where n is the number of nodes in the linked list
#Overall space complexity: O(n), where n is the number of nodes in the linked list.
#This is due to the function calls building up on the implicit call stack.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        previous = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return previous
