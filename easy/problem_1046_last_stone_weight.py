"""This is my solution to Leetcode problem 1046."""


from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index, weight in enumerate(stones):
            stones[index] = -weight
        heapify(stones)
        while len(stones) > 1:
            heaviest_stone = heappop(stones)
            second_heaviest_stone = heappop(stones)
            if heaviest_stone != second_heaviest_stone:
                heaviest_stone -= second_heaviest_stone
                heappush(stones, heaviest_stone)
        if stones:
            return abs(stones[0])
        return 0


#Overall time complexity: O(nlogn), where "n" is the number of stones

#Explanation: First to overcome the fact the Python's heapq module only
#supports min heaps, you first have to change the sign of all of the values in
#stones (takes O(n) time). Next you call heapify on stones (takes O(n) time).
#Afterwards you loop until the list is either of size 1, or empty, calling heappop
#to get the two heaviest stones. If their values are not equal, you subtract the value
#of the smaller stone from the larger stone and insert the larger stone back into the heap (O(logn) time).
#Since the max amount of times the loop runs in O(n) and all major operations in the loop take O(logn) time,
#the time complexity for the loop is O(nlogn). This makes the time complexity O(n + n + nlogn), which resolves
#to O(nlogn) since this is the greater order time complexity.

#Overall space complexity: O(1)
