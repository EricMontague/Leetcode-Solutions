"""This file contains my solution to Leetcode problem 234: Palindrome Linked List."""


# time complexity: O(n), where 'n' is the number of nodes in the linked list
# space complexity: O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        middleNode = self.getMiddleNode(head)
        tail = self.reverseSubList(middleNode)
        return self.checkPalindrome(head, tail)
    
    def getMiddleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseSubList(self, node):
        previous = None
        current = node
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        return previous
    
    def checkPalindrome(self, head, tail):
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
    