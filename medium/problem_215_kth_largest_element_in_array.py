"""This file contains my solutions to Leetcode prob lem 215: Kth Largest Element in Array."""

# Quick Select Solution - Hoare's partitioning algorithm
# time complexity: O(n), best and average cases, O(n ^2) worst case
# space complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        kth_largest_index = len(nums) - k
        while start != end:
            split_index = self.partition(nums, start, end)
            if split_index < kth_largest_index:
                start = split_index + 1
            else:
                end = split_index
        return nums[start]
    
    def partition(self, nums, start, end):
        pivot_index = start + (end - start) // 2
        pivot_value = nums[pivot_index]
        left = start
        right = end
        while True:
            while nums[left] < pivot_value:
                left += 1
            while nums[right] > pivot_value:
                right -= 1
            if left >= right:
                return right
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    


# Max Heap Solution
# time complexity: O(n + klogn), where 'n' is the number of integers and 'k' is the paramater k
# space complexity: O(1)
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.flip_integer_signs(nums)
        heapq.heapify(nums)
        return self.get_kth_largest_element(nums, k)
    
    def flip_integer_signs(self, nums):
        for index in range(len(nums)):
            nums[index] = nums[index] * -1
            
    def get_kth_largest_element(self, nums, k):
        kth_largest_element = float("inf")
        for num in range(k):
            kth_largest_element = heapq.heappop(nums)
        return kth_largest_element * -1
        

# Min Heap Solution
# time complexity: O(nlogk)
# space complexity: O(k)

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    
