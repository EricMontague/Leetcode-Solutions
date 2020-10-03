"""This is my solution to Leetcode problem 692: Top K Frequent Words."""


# Quickselect solution
# time complexity: O(n + klogk)
# space complexity: O(n)
import random
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = Counter(words)
        unique_words = list(word_counter.keys())
        kth_most_frequent_word_index = self.find_kth_most_frequent_word_index(
            unique_words, word_counter, 0, len(unique_words) - 1, k
        )
        k_most_frequent_words = unique_words[kth_most_frequent_word_index:]
        k_most_frequent_words.sort(key=lambda w: (-word_counter[w], w))
        return k_most_frequent_words
    
    def find_kth_most_frequent_word_index(self, words, word_counter, start, end, k):
        if start == end:
            return start
        pivot_index = self.partition(words, word_counter, start, end)
        kth_most_frequent_index = len(words) - k
        if pivot_index == kth_most_frequent_index:
            return pivot_index
        elif pivot_index < kth_most_frequent_index:
            return self.find_kth_most_frequent_word_index(
                words, word_counter, pivot_index + 1, end, k
            )
        else:
            return self.find_kth_most_frequent_word_index(
                words, word_counter, start, pivot_index - 1, k
            )
    
    def partition(self, words, word_counter, start, end):
        self.randomize_pivot_index(words, start, end)
        pivot_value_count = word_counter.get(words[end])
        pivot_index = start
        for index in range(start, end):
            word_count = word_counter.get(words[index])
            if word_count == pivot_value_count:
                if words[index] > words[end]:
                    words[index], words[pivot_index] = (
                        words[pivot_index], words[index]    
                    )
                    pivot_index += 1
            elif word_count < pivot_value_count:
                words[index], words[pivot_index] = words[pivot_index], words[index]
                pivot_index += 1
        words[pivot_index], words[end] = words[end], words[pivot_index]
        return pivot_index
    
    def randomize_pivot_index(self, words, start, end):
        random_pivot_index = random.randint(start, end)
        words[random_pivot_index], words[end] = words[end], words[random_pivot_index]
        

# time complexity: O(nlogk), where 'n' is the number of words and 'k' is the
# parameter we're given
# space complexity: O(n)
import heapq
from collections import Counter

class PriorityQueueItem:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __lt__(self, other_item):
        if self.key == other_item.key:
            return self.value > other_item.value
        return self.key < other_item.key
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        priority_queue = self.build_priority_queue(word_counts, k)
        return self.get_top_k_frequent_words(priority_queue)
    
    def build_priority_queue(self, word_counts, k):
        priority_queue = []
        for word, count in word_counts.items():
            queue_item = PriorityQueueItem(count, word)
            heapq.heappush(priority_queue, queue_item)
            if len(priority_queue) > k:
                heapq.heappop(priority_queue)
        return priority_queue
    
    def get_top_k_frequent_words(self, priority_queue):
        top_k_frequent_words = []
        while priority_queue:
            queue_item = heapq.heappop(priority_queue)
            top_k_frequent_words.append(queue_item.value)
        return top_k_frequent_words[::-1]


import heapq
from collections import Counter

class PriorityQueueItem:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __gt__(self, other_item):
        if self.key == other_item.key:
            return self.value > other_item.value
        return self.key > other_item.key
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        priority_queue = self.build_priority_queue(word_counts, k)
        return self.get_top_k_frequent_words(priority_queue, k)
    
    def build_priority_queue(self, word_counts, k):
        priority_queue = [
            PriorityQueueItem(-count, word) 
            for word, count in word_counts.items()
        ]
        heapq.heapify(priority_queue)
        return priority_queue
    
    def get_top_k_frequent_words(self, priority_queue, k):
        top_k_frequent_words = []
        for num in range(k):
            queue_item = heapq.heappop(priority_queue)
            top_k_frequent_words.append(queue_item.value)
        return top_k_frequent_words