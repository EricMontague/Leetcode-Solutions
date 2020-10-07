"""This file contains my solutions to Leetcode problem 61: Rotate List."""


# time complexity: O(n), where 'n' is the number of nodes in the list
# space complexity: O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        num_nodes = self.count_nodes(head)
        num_moves = k % num_nodes
        if num_moves == 0:
            return head
        first_tail = None
        second_tail = None
        first = head
        second = head
        for move in range(num_moves):
            second_tail = second
            second = second.next
        while second:
            second_tail = second
            second = second.next
            first_tail = first
            first = first.next
        first_tail.next = None
        second_tail.next = head
        return first
    
    def count_nodes(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
        

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        num_nodes = self.connect_tail_to_head(head)
        num_moves = num_nodes - k % num_nodes - 1
        current = head
        for move in range(num_moves):
            current = current.next
        new_head = current.next
        current.next = None
        return new_head
    
    def connect_tail_to_head(self, head):
        num_nodes = 1
        current = head
        while current.next:
            num_nodes += 1
            current = current.next
        current.next = head
        return num_nodes