"""This file contains my solution to Leetcode problem 1492: The kth factor of N."""


# Max Heap Solution
# time complexity: O(sqrt(n) * logk), where 'n' is num and 'k' is the variable 'k'
# space complexity: O(k)
import heapq
import math

class Solution:
    def kthFactor(self, num: int, k: int) -> int:
        max_heap = []
        for factor in range(1, math.floor(math.sqrt(num)) + 1):
            if num % factor == 0:
                heapq.heappush(max_heap, factor * -1)
                other_factor = num // factor
                if other_factor != factor:
                    heapq.heappush(max_heap, other_factor * -1)
                while len(max_heap) > k:
                    heapq.heappop(max_heap)
        if len(max_heap) < k:
            return -1
        return max_heap[0] * -1



# Min Heap Solution
# time complexity: O(sqrt(n)* log sqrt(n))
# space complexity: O(sqrt(n))
import heapq
import math

class Solution:
    def kthFactor(self, num: int, k: int) -> int:
        min_heap = []
        for factor in range(1, math.floor(math.sqrt(num)) + 1):
            if num % factor == 0:
                min_heap.append(factor)
                other_factor = num // factor
                if other_factor != factor:
                    min_heap.append(other_factor)
        heapq.heapify(min_heap)
        return self.get_kth_factor(min_heap, k)
    
    def get_kth_factor(self, min_heap, k):
        if len(min_heap) < k:
            return -1
        factor = None
        for index in range(k):
            factor = heapq.heappop(min_heap)
        return factor



# Simple iterative solution
# time complexity: O(sqrt(n))
# space complexity: O(sqrt(n))
class Solution:
    def kthFactor(self, num: int, k: int) -> int:
        lower_divisors = []
        higher_divisors = []
        sqrt = 1 / 2
        for divisor in range(1, int(num ** sqrt) + 1):
            if num % divisor == 0:
                lower_divisors.append(divisor)
                other_divisor = num // divisor
                if other_divisor != divisor:
                    higher_divisors.append(other_divisor)
        num_lower_divisors = len(lower_divisors)
        num_higher_divisors = len(higher_divisors)
        if k > num_lower_divisors + num_higher_divisors:
            return -1
        if k <= num_lower_divisors:
            return lower_divisors[k - 1]
        return higher_divisors[(k - num_lower_divisors) * -1]