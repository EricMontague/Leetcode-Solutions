"""This is my solution to Leetcode problem 817."""


#Overall time complexity: O(n), where "n" is the number of nodes in the linked list
#Overall space complexity: O(m), where "m" is the number of integers in "G"
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        numberOfComponents = 0
        linkedListValues = set(G)
        start = head
        while start is not None:
            if start.val in linkedListValues:
                end = start
                while end is not None and end.val in linkedListValues:
                    end = end.next
                numberOfComponents += 1
                start = end
            else:
                start = start.next
        return numberOfComponents


#Intuition:
#Convert "G" into a set to make lookups constant time.
#First, loop until you find the start of a connected component. A node is in a connected
#component if it is in the set, "G". Once you find the start of a connected component,
#define another variable named end, and search for the end of a connected component.
#You know that a component has ended if the next node in the list is not in the set,
#or if you are at the last node in the list.

#Once you exit this inner while loop, increment the number of components by 1, and set start
#equal to end so that you can begin the search for a new connected component
    