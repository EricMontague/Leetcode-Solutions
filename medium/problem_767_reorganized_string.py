"""This file contains my solutions from Leetcode problem 767: Reorganize string."""



# time complexity: O(NlogA), where 'N' is the size of the string
# and 'A' is the size of the alphabet. Here our alphabet is stated to
# be all lowercase letters, so the time complexity is really O(N)

# space complexity: O(N)
import heapq

class Solution:
    def reorganizeString(self, string: str) -> str:
        if not string:
            return ""
        alphabet_size = 26
        character_counts = self.build_character_counts(string, alphabet_size)
        max_heap = self.build_max_heap(character_counts)
        max_character_count = max_heap[0][0] * -1
        if max_character_count > (len(string) + 1) // 2:
            return ""
        return self.build_reorganized_string(max_heap)
    
    def build_character_counts(self, string, alphabet_size):
        counts = [0] * alphabet_size
        for character in string:
            index = ord(character) - ord("a")
            counts[index] += 1
        return counts
    
    def build_max_heap(self, character_counts):
        max_heap = []
        for index, count in enumerate(character_counts):
            if count > 0:
                heap_item = (-count, chr(ord("a") + index))
                heapq.heappush(max_heap, heap_item)
        return max_heap
    
    def build_reorganized_string(self, max_heap):
        reorganized_characters = []
        while len(max_heap) > 1:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)
            reorganized_characters.append(char1)
            reorganized_characters.append(char2)
            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))
        if max_heap:
            count, char = heapq.heappop(max_heap)
            reorganized_characters.append(char)
        return "".join(reorganized_characters)