from heapq import heappush, heappop
from collections import Counter

#My original solution
class Solution:
    def frequencySort(self, s: str) -> str:
        #if check not necessary for this problem,
        #but it's good to practice for edge cases
        if s is None or len(s) < 1:
            return ""
        priority_queue = []
        counts = Counter(s)
        self.build_queue(priority_queue, counts)
        chars = self.extract_chars(priority_queue)
        return chars
        
    def build_queue(self, priority_queue, counts):
        for char, count in counts.items():
            heappush(priority_queue, (-count, char))
            
    def extract_chars(self, priority_queue):
        chars = ""
        while priority_queue:
            item = heappop(priority_queue)
            chars += (abs(item[0]) * item[1]) #O(n)
        return chars

#Tricks: You can turn Python's heapq into a max heap by making the keys negative

#Overall time complexity: O(nlogn), where n is the number of characters
#in the input string

#Explanation: Constructing the frequency dictionary using Counter will take O(n) time,
#because you need to iterate over each character in "s" to build it. The build_queue()
#method will take O(klogk) time, where "k" is the distinct number of characters in the input
#string, "s" as you have to iteratie over all k characters and inserting into a min heap
#takes O(logk) time. The last method, extract_chars() will take O(klogk + n), where "k" is the
#same as in build_queue() and "n" is the number of chars in the string due to the sum of the
#number of concatenations. 
#Putting this together gives us O(n + klogk + klogk + n), which reduces to O(n + klogk). However,
#in the worst case scenario of inputs, every character in "s" is distinct, meaning that k == n, so
#this is better expressed as O(n + nlogn), and after dropping the lower order terms, wer get O(nlogn)

#Overall space complexity: O(n), where n is the number of characters in the input string.

#The space complexity for the counter is O(k), where k is the distinct number of characters in the input string.
#The priority queue also holds all distinct characters, so this is O(k) as well. Lastly, the chars variable
#in extract_chars() will eventually consist of all n characters in the input string, so that is O(n).
#This gives a space complexity of O(2k + n), which leads to O(k + n). But this can better be expressed as
#O(n) in the worst case, like discussed above.


#######################################
# Better solution below
#######################################

#The below solution achieves the same overall time and space complexity as the one above,
#but it is not mine. I simply refactored my answer based on what I thought wa a better 
#implementation from Leetcode's discussions. The main differences include what are the
#object oriented approach, the O(n) time complexity of build_queue() through using heapify (still doesn't)
#affect the overall O(nlogn) time complexity, and the combination of a min heap with a deque to
#achieve the desired order isn't of my hack for turning heapq into a max heap.

#Note: the person who submitted this is wrong on their time complexity analysis as they do not account for the nglon
#removal at the end of the algorithm. The time complexity is definitely O(nlogn)
#source: https://leetcode.com/problems/sort-characters-by-frequency/discuss/404046/Python-O(n)-Bucket-Sort-and-Min-heap


from heapq import heapify, heappop
from collections import Counter, deque


class QueueItem:
    def __init__(self, key, count):
        self.key = key
        self.count = count
        
    def __lt__(self, other):
        return self.count < other.count


class Solution:
    def frequencySort(self, s: str) -> str:
        if s is None or len(s) < 1:
            return ""
        counts = Counter(s)
        priority_queue = self.build_queue(counts)
        chars = self.extract_chars(priority_queue)
        return chars
        
    def build_queue(self, counts):
        priority_queue = [QueueItem(key, count) for key, count in counts.items()]
        heapify(priority_queue)
        return priority_queue
            
    def extract_chars(self, priority_queue):
        char_deque = deque()
        while priority_queue:
            item = heappop(priority_queue)
            char_deque.appendleft(abs(item.count) * item.key)
        return "".join(char_deque)


