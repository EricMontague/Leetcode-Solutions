"""This file contains my solution to Leetcode problem 143: Reorder List."""


# time complexity: O(n), where 'n' is the number of nodes in the linked list
# space complexity: O(n), where 'n' is the number of nodes in the linked list
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            nodes = self.getNodes(head)
            return self.reorderNodes(nodes)
    
    def getNodes(self, head):
        nodes = []
        current = head
        while current is not None:
            nodes.append(current)
            current = current.next
        return nodes
    
    def reorderNodes(self, nodes):
        sentinel = ListNode(-1, None)
        previous = sentinel
        low = 0
        high = len(nodes) - 1
        while low < high:
            previous.next = nodes[low]
            nodes[low].next = nodes[high]
            previous = nodes[high]
            low += 1
            high -= 1
        if low == high:
            previous.next = nodes[low]
        nodes[low].next = None
        

# More space efficient solution

# time complexity: O(n), where 'n' is the number of nodes in the linked list
# space complexity: O(1)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            middleNode = self.findMiddleNode(head)
            tail = self.reverseNodes(middleNode)
            self.reorderNodes(head, tail)
    
    def findMiddleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseNodes(self, node):
        previous = node
        current = node.next
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        return previous
    
    def reorderNodes(self, head, tail):
        sentinel = ListNode(-1, None)
        lastNode = sentinel
        while head != tail and head.next != tail:
            next_ = head.next
            lastNode.next = head
            head.next = tail
            lastNode = lastNode.next.next
            head = next_
            tail = tail.next
        lastNode.next = head
        tail.next = None
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            middleNode = self.findMiddleNode(head)
            tail = self.reverseNodes(middleNode)
            self.reorderNodes(head, tail)
    
    def findMiddleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseNodes(self, node):
        previous = node
        current = node.next
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        return previous
    
    def reorderNodes(self, head, tail):
        sentinel = ListNode(-1, None)
        lastNode = sentinel
        while head != tail and head.next != tail:
            next_ = head.next
            lastNode.next = head
            head.next = tail
            lastNode = lastNode.next.next
            head = next_
            tail = tail.next
        lastNode.next = head
        tail.next = None
        