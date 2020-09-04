"""This is my solution to Leetcode problem 23."""


import heapq


class QueueItem:
    
    def __init__(self, key, index):
        self.key = key
        self.index = index
        
    def __lt__(self, other):
        if self.key == other.key:
            return self.index < other.index
        return self.key < other.key

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        priorityQueue = self.buildPriorityQueue(lists)
        return self.mergeLists(priorityQueue, lists)
        
    def buildPriorityQueue(self, lists):
        priorityQueue = []
        for index in range(len(lists)):
            node = lists[index]
            if node:
                queueItem = QueueItem(node.val, index)
                priorityQueue.append(queueItem)
        heapq.heapify(priorityQueue)
        return priorityQueue
    
    def mergeLists(self, priorityQueue, lists):
        sentinel = ListNode(None, None)
        newTail = sentinel
        while priorityQueue:
            queueItem = heapq.heappop(priorityQueue)
            newTail.next = lists[queueItem.index]
            newTail = newTail.next
            lists[queueItem.index] = lists[queueItem.index].next
            newCurrentNode = lists[queueItem.index]
            if newCurrentNode is not None:
                heapq.heappush(priorityQueue, QueueItem(newCurrentNode.val, queueItem.index))
        return sentinel.nextlists[index].val, index))
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
