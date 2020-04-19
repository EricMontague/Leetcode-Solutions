"""This is my solution to Leetcode problem 23."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        tail = ListNode(None)
        head = tail
        min_heap = []
        for index, node in enumerate(lists):
            if node is not None:
                heappush(min_heap, (node.val, index))
        while min_heap:
            node_value, index = heappop(min_heap)
            tail.next = lists[index]
            tail = tail.next
            lists[index] = lists[index].next
            if lists[index] is not None:
                heappush(min_heap, (lists[index].val, index))
        return head.next

#Overall time complexity: O(Nlogk), where "N" is the total number of nodes in
#all linked lists and where "k" is the number of linked lists.

#Intuition:
#This question is similar to the merge process during merge sort. You compare
#the smallest unsorted value in each list and choose the smallest out of all of those.
#Then, you move forward one step in the list of the value you just chose.
#This solution does that but instead uses a min heap. First you create a heap that contains
#all of the head nodes of each linked list. Then in the loop applies the general process described
#above using the heap to keep track of what the next smallest value will be.

#Overall space complexity: O(k), where "k" is the number of linked lists.
#This solution maintains a min heap that is at most size "k". 
