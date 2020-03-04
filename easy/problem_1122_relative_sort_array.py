"""My solution to Problem 1122: Relative  Sort Array."""

from heapq import heappush, heappop
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        heap = []
        arr2_positions = {}
        arr2_length = len(arr2)
        for index, num in enumerate(arr2):
            arr2_positions[num] = index
        for num in arr1:
            if num in arr2_positions:
                heappush(heap, (arr2_positions[num], num))
            else:
                heappush(heap, (arr2_length, num))
        output = []
        while heap:
            item = heappop(heap)
            output.append(item[1])
        return output

#Overall time complexity: O(nlogn), where n is the number of elements in the first array

#Explanation: The first for loop take O(m) time where m is the number of elements in the
#second array. The second loop takes O(nlogn), because you have to loop through all n
#elements in the second array, you perform an insert operation on each loop. Inserting into
#a min heap is O(logn). Finally, you loop through all n elements in the heap, popping each
#one off and adding the element to the list, which is also O(nlogn). This makes the time complexity
#O(2nlogn + m), but since we drop coefficients and lower order terms, this is reduced to O(nlogn).

#space complexity: O(n)
#Explanation: The size of arr2_positions will be O(m), and between output and heap, the
#space complexity will be O(n). Thus, the space comeplexity will be O(n + m). But,
#since m is upper bounded by n, in the worst case this could be said to be O(n).



###################################################
#Below is a more objected oriented and modularized solution
#Overall time and space complexities are the same.
###################################################


from heapq import heapify, heappop
from collections import deque


class QueueItem:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        
    def __lt__(self, other):
        if self.key == other.key:
            return self.data < other.data
        return self.key < other.key
    
    
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_positions = self.build_dictionary(arr2)
        priority_queue = self.build_queue(arr1, arr2, arr2_positions)
        return self.extract_items(priority_queue)
        
    def build_dictionary(self, arr2):
        arr2_positions = {}
        for index, num in enumerate(arr2):
            arr2_positions[num] = index
        return arr2_positions
    
    def build_queue(self, arr1, arr2, arr2_positions):
        arr2_length = len(arr2)
        priority_queue = []
        for num in arr1:
            if num in arr2_positions:
                priority_queue.append(QueueItem(arr2_positions[num], num))
            else:
                priority_queue.append(QueueItem(arr2_length, num))
        heapify(priority_queue)
        return priority_queue
    
    def extract_items(self, priority_queue):
        output = []
        while priority_queue:
            item = heappop(priority_queue)
            output.append(item.data)
        return output
