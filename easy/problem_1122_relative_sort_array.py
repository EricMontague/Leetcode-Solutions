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
