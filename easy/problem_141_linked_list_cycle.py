"""These are my solutions to Leetcode problem 141."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Suboptimal Solution
#Overall time complexity: O(n), where "n" is the number of nodes in the linked list
#Overall space complexity: O(n), where "n" is the number of nodes in the linked list
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        current = head
        while current is not None:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False

#Optimal Solution
#Overall time complexity: O(n), where "n" is the number of nodes in the linked list
#Overall space complexity: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        