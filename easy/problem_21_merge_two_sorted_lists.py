"""This is my solution to Leetcode problem 21: Merge Two Sorted Lists."""


# time complexity: O(n + m), where 'n' is the length of the first list and
# 'm' is the length of the second list
# space complexity: O(1)


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        sentinelNode = ListNode(-1, None)
        newTail = sentinelNode
        left = list1
        right = list2
        while left and right:
            if left.val <= right.val:
                newTail.next = left
                left = left.next
            else:
                newTail.next = right
                right = right.next
            newTail = newTail.next
        
        if left is None:
            newTail.next = right
        else:
            newTail.next = left
        return sentinelNode.next