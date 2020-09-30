"""This file contains my solutions to Leetcode problem 328: Odd Even Linked List."""



# time complexity : O(n), where 'n' is the number of nodes in the linekd list
# space complexity: O(1)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        oddHead = head
        oddTail = oddHead
        evenHead = head.next
        evenTail = evenHead
        counter = 3
        current = head.next.next
        while current:
            if counter % 2 == 0:
                evenTail.next = current
                evenTail = evenTail.next
            else:
                oddTail.next = current
                oddTail = oddTail.next
            counter += 1
            current = current.next
        evenTail.next = None
        oddTail.next = evenHead
        return oddHead


# Slightly more elegant solution.
# same time and space complexities
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        currentOdd = head
        currentEven = head.next
        evenHead = currentEven
        while currentEven and currentEven.next:
            currentOdd.next = currentOdd.next.next
            currentEven.next = currentEven.next.next
            currentOdd = currentOdd.next
            currentEven = currentEven.next
        currentOdd.next = evenHead
        return head