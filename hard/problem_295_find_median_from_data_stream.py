"""This file contains my solutions to Leetcode problem 295: Find Median from Data Stream."""


import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.lower_half = []
        self.upper_half = []
        

    def addNum(self, num: int) -> None:
        median = self.findMedian()
        if num < median:
            heapq.heappush(self.lower_half, num * -1)
        else:
            heapq.heappush(self.upper_half, num)
        self.size += 1
        self.rebalance()
    
    def rebalance(self):
        if len(self.lower_half) < self.size // 2:
            middle_num = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, middle_num * -1)
        elif len(self.lower_half) > self.size // 2:
            middle_num = heapq.heappop(self.lower_half) * -1
            heapq.heappush(self.upper_half, middle_num)
            
    def findMedian(self) -> float:
        if self.size == 0:
            return 0
        if self.size % 2 == 0:
            lower = self.lower_half[0] * -1
            upper = self.upper_half[0]
            return (lower + upper) / 2
        return self.upper_half[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()