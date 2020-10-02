"""This file contains my solutions to Leetcode problem 347: Top K Frequent Elements."""


# Solution based on Bucket sort
# time complexity: O(n), where 'n' is the number of elements
# space complexity: O(n)

from collections import Counter

class Solution:
    def topKFrequent(self, elements: List[int], k: int) -> List[int]:
        frequencyMatrix = self.createFrequencyMatrix(len(elements))
        elementCounts = Counter(elements)
        self.groupElementsByFrequency(elementCounts, frequencyMatrix)
        return self.getTopKFrequentElements(frequencyMatrix, k)
    
    def createFrequencyMatrix(self, numberOfRows):
        frequencyMatrix = [[] for index in range(numberOfRows)]
        return frequencyMatrix
    
    def groupElementsByFrequency(self, elementCounts, frequencyMatrix):
        for element, count in elementCounts.items():
            frequencyMatrix[count - 1].append(element)
    
    def getTopKFrequentElements(self, frequencyMatrix, k):
        topKFrequentElements = []
        for bucket in reversed(frequencyMatrix):
            for element in bucket:
                if k == 0:
                    break
                topKFrequentElements.append(element)
                k -= 1
            if k == 0:
                break
        return topKFrequentElements

# QuickSelect solution
# time complexity: Best and average cases: O(n), where 'n' is the number of elements.
# Worst case is O(n ^ 2), due to picking a bad pivot in Quickselect

# space complexity: O(n)
import random
from collections import Counter


class Solution:
    def topKFrequent(self, elements: List[int], k: int) -> List[int]:
        elementCounts = Counter(elements)
        uniqueElements = list(elementCounts.keys())
        kthLargestIndex = self.findKthMostFrequentElement(uniqueElements, elementCounts, k)
        return uniqueElements[kthLargestIndex:]
    
    def findKthMostFrequentElement(self, elements, elementCounts, k):
        numElements = len(elements)
        start = 0
        end = numElements - 1
        while start < end:
            pivotIndex = self.partition(elements, start, end, elementCounts)
            kthMostFrequentIdx = numElements - k
            if pivotIndex == kthMostFrequentIdx:
                return pivotIndex
            elif pivotIndex < kthMostFrequentIdx:
                start = pivotIndex + 1
            else:
                end = pivotIndex - 1
        return start
    
    def partition(self, elements, start, end, elementCounts):
        self.randomizePivot(elements, start, end)
        pivotValueCount = elementCounts.get(elements[end])
        pivotIndex = start
        for index in range(start, end):
            elementCount = elementCounts.get(elements[index])
            if elementCount <= pivotValueCount:
                elements[pivotIndex], elements[index] = (
                    elements[index], elements[pivotIndex]
                )
                pivotIndex += 1
        elements[pivotIndex], elements[end] = (
            elements[end], elements[pivotIndex]
        )
        return pivotIndex
    
    def randomizePivot(self, elements, start, end):
        randomPivotIndex = random.randint(start, end)
        elements[randomPivotIndex], elements[end] = (
            elements[end], elements[randomPivotIndex]
        )
    
    


# time complexity: O(n + klogn), where 'n' is the number of elements in the list and
# 'k' is the parameter we're given

# space complexity: O(n)

import heapq
from collections import Counter

class PriorityQueueItem:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __gt__(self, otherItem):
        if self.key == otherItem.key:
            return self.value > otherItem.value
        return self.key > otherItem.key

class Solution:
    def topKFrequent(self, elements: List[int], k: int) -> List[int]:
        if len(elements) == k:
            return elements
        elementCounts = Counter(elements)
        priorityQueue = self.buildPriorityQueue(elements, elementCounts)
        return self.getTopKFrequentElements(priorityQueue, k)
    
    def buildPriorityQueue(self, elements, elementCounts):
        priorityQueue = []
        for element in elements:
            if element in elementCounts:
                item = PriorityQueueItem(-elementCounts[element], -element)
                priorityQueue.append(item)
                elementCounts.pop(element)
        heapq.heapify(priorityQueue)
        return priorityQueue
    
    def getTopKFrequentElements(self, priorityQueue, k):
        topKFrequentElements = []
        for num in range(k):
            item = heapq.heappop(priorityQueue)
            topKFrequentElements.append(item.value * -1)
        return topKFrequentElements



# time complexity: O(nlogk), where 'n' is the number of elements in the list and 'k'
# is the parameter we're given

# space complexity: O(n + k)
import heapq
from collections import Counter

class PriorityQueueItem:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, otherItem):
        if self.key == otherItem.key:
            return self.value < otherItem.value
        return self.key < otherItem.key

class Solution:
    def topKFrequent(self, elements: List[int], k: int) -> List[int]:
        if len(elements) == k:
            return elements
        elementCounts = Counter(elements)
        priorityQueue = self.buildPriorityQueue(elements, elementCounts, k)
        return self.getTopKFrequentElements(priorityQueue, k)
    
    def buildPriorityQueue(self, elements, elementCounts, k):
        priorityQueue = []
        for element in elements:
            if element in elementCounts:
                item = PriorityQueueItem(elementCounts[element], element)
                heapq.heappush(priorityQueue, item)
                if len(priorityQueue) > k:
                    heapq.heappop(priorityQueue)    
                elementCounts.pop(item.value)
        return priorityQueue
    
    def getTopKFrequentElements(self, priorityQueue, k):
        topKFrequentElements = []
        for num in range(k):
            item = heapq.heappop(priorityQueue)
            topKFrequentElements.append(item.value)
        return topKFrequentElements