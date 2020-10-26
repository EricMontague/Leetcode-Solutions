"""This file contains my solutions from Leetcode problem 767: Reorganize string."""



# Hash table solution
# time complexity: O(n + a), where 'n' is the number of characters in the string
# 'a' is the size of your alphabet. If 'a' is constant, then this becomes O(n)

# space complexity: O(n + a). Same explanation as above
class Solution:
    
    ALPHABET_START = "a"
    ALPHABET_SIZE = 26
    def reorganizeString(self, string: str) -> str: 
        string_length = len(string)
        
        # Build character frequency list
        char_counts, max_count_index = self.build_char_counts(string)
        
        # Constraint check
        if char_counts[max_count_index] > (string_length + 1) // 2:
            return ""
        return self.build_reorganized_string(char_counts, max_count_index, string_length)
    
    def build_char_counts(self, string):
        char_counts = [0] * self.ALPHABET_SIZE
        max_count = 0
        max_count_index = -1
        for character in string:
            index = ord(character) - ord(self.ALPHABET_START)
            char_counts[index] += 1
            if max_count < char_counts[index]:
                max_count = char_counts[index]
                max_count_index = index
        return char_counts, max_count_index
    
    def build_reorganized_string(self, char_counts, max_count_index, string_length):
        # Fill in character with highest frequency first
        reorganized_chars = [None] * string_length
        current = self.fill_characters(reorganized_chars, char_counts, max_count_index, 0)
        
        # Fill in the rest of the characters
        for char_index in range(self.ALPHABET_SIZE):
            # Ignore the character that has the highest frequency
            # Since we already filled it in
            if char_index == max_count_index:
                continue
            current = self.fill_characters(
                reorganized_chars,
                char_counts,
                char_index,
                current
            )
        return "".join(reorganized_chars)
    
    def fill_characters(self, reorganized_chars, char_counts, char_index, start):
        for j in range(char_counts[char_index]):
            if start >= len(reorganized_chars):
                start = 1
            reorganized_chars[start] = chr(ord(self.ALPHABET_START) + char_index)
            start += 2
        return start
        
        
    
            

# Max Heap Solution
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




# Sorting Solution
# time complexity: O(nlogn). where 'n' is the number of characters in string
# space complexity: O(n + min(n, a)), where 'a' is the size of the alphabet
from collections import Counter

class Solution:
    def reorganizeString(self, string: str) -> str:
        if not string:
            return ""
        char_counts = Counter(string)
        sorted_chars = sorted(string, key=lambda s: (-char_counts[s], s))
        reorganized_chars = [None] * len(string)
        slow = 0
        fast_starting_point = 0
        while slow < len(string):
            fast = fast_starting_point
            while (
                slow < len(string) 
                and fast < len(string) 
                and reorganized_chars[fast] is None
            ):
                char = sorted_chars[slow]
                char_count = char_counts.get(char)
                if char_count:
                    char_counts.pop(char)
                    if char_count > (len(string) + 1) // 2:
                        return ""
                reorganized_chars[fast] = char
                slow += 1
                fast += 2
            fast_starting_point += 1
        return "".join(reorganized_chars)




        