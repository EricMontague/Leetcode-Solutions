"""This is my solution to Leetcode problem 692: Top K Frequent Words."""


from heapq import heappop, heapify, heappush


class MaxHeapItem:
    
    def __init__(self, key, data):
        self.key = key
        self.data = data
        
    def __gt__(self, other):
        if self.key == other.key:
            return self.data > other.data
        return self.key > other.key
    

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if k < 1 or not words:
            return []
        frequencies = self.calculate_word_frequencies(words)
        max_heap = self.build_max_heap(frequencies, k)
        return self.get_top_k_frequent(max_heap, k)
    
    def calculate_word_frequencies(self, words):
        frequencies = {}
        for word in words:
            frequencies.setdefault(word, 0)
            frequencies[word] += 1
        return frequencies
    
    def build_max_heap(self, frequencies, k):
        max_heap = [MaxHeapItem(-frequency, word) for word, frequency in frequencies.items()]
        heapify(max_heap)
        return max_heap
    
    def get_top_k_frequent(self, max_heap, k):
        elements = [heappop(max_heap).data for index in range(k)]
        return elements
        

#Overall time complexity: O(n + klogn), where "n" is the number of words and "k"
#is the top "k" most frequent words

#Explanation: It takes O(n) time to store all "n" words into the frequencies dictionary. In the worst
#case, every word in the list will be unique so, iterating over all "n" elements in the dictionary and 
# appending to a list takes O(n) time. Next, heapify takes O(n) time. Finally, the last method takes O(klogn) 
# time because you have to loop "k" times and getting the maximum element out of a max heap takes O(log n) time. 
# This makes the time complexity O(3n + klogn) which is just O(n + klogn).

#Overall space complexity: O(n)
#Explanation: In the worst case, every word in the list is unique, so the frequencues
#dictionary would contain all "n" words. Also, the second method stores
#all "n" elements into the max heap, making for O(n + n), which is just O(n).


#Note: Another way to do this is to use a min heap that always maintains a size of "k",
#but that solution runs in O(nlog k) time, which is slightly worse.
