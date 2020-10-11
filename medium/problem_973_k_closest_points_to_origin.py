"""This file contains my solutions to Leetcode problem 973: K Closest Points to Origin."""


# Min Heap Solution
# time complexity: O(n + klogn)
# space complexity: O(n)

import heapq, math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0 or not points:
            return []
        min_heap = self.build_min_heap(points, k)
        return self.get_k_closest_points(min_heap, k)

    def build_min_heap(self, points, k):
        min_heap = []
        source = [0, 0]
        for point in points:
            distance = self.calculate_euclidean_distance(source, point)
            min_heap.append((distance, point))
        heapq.heapify(min_heap)
        return min_heap

    def calculate_euclidean_distance(self, source, destination):
        return math.sqrt(
            (destination[0] - source[0]) ** 2 + (destination[1] - source[1]) ** 2
        )
    
    def get_k_closest_points(self, min_heap, k):
        k_closest_points = []
        for num in range(k):
            distance, point = heapq.heappop(min_heap)
            k_closest_points.append(point)
        return k_closest_points

# Max Heap Solution

# time complexity: O(nlogk), where 'n' is the number of points and 'k'
# is the parameter

# space complexity: O(k)
import heapq, math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0 or not points:
            return []
        max_heap = self.build_max_heap(points, k)
        k_closest_points = [point for distance, point in max_heap]
        return k_closest_points

    def build_max_heap(self, points, k):
        max_heap = []
        source = [0, 0]
        for point in points:
            distance = self.calculate_euclidean_distance(source, point)
            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return max_heap

    def calculate_euclidean_distance(self, source, destination):
        return math.sqrt(
            (destination[0] - source[0]) ** 2 + (destination[1] - source[1]) ** 2
        )


# Quickselect Solution
# time complexity: O(n)
# space complexity: O(k)

class Solution:
    
    ORIGIN = [0, 0]
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0 or not points:
            return []
        kth_closest_point = self.find_kth_closest_from_origin(
            points, k
        )
        return points[0: kth_closest_point + 1]
    
    def find_kth_closest_from_origin(self, points, k):
        start = 0
        end = len(points) - 1
        while start != end:
            split_index = self.partition(points, start, end)
            kth_closest_index = k - 1
            if split_index < kth_closest_index:
                start = split_index + 1
            else:
                end = split_index
        return start
    
    def partition(self, points, start, end):
        low = start
        high = end
        pivot_index = low + (high - low) // 2
        pivot_value_distance = self.calculate_euclidean_distance(
            self.ORIGIN, points[pivot_index]
        )
        while True:
            while self.calculate_euclidean_distance(self.ORIGIN, points[low]) < pivot_value_distance:
                print(low)
                low += 1
            while self.calculate_euclidean_distance(self.ORIGIN, points[high]) > pivot_value_distance:
                high -= 1
            if low >= high:
                return high
            points[low], points[high] = points[high], points[low]
            low += 1
            high -= 1
            
    def calculate_euclidean_distance(self, source, destination):
        return math.sqrt(
            (destination[0] - source[0]) ** 2 
            + (destination[1] - source[1]) ** 2
        )