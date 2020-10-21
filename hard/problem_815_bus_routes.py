"""This file contains my solutions to Leetcode problem 815: Bus Routes."""


from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], start: int, end: int) -> int:
        if not routes or start == end:
            return 0
        route_stop_mapping, stop_route_mapping = self.create_mappings(routes)
        if start not in stop_route_mapping or end not in stop_route_mapping:
            return 0
        queue, visited = self.find_initial_routes(start, stop_route_mapping)
        while queue:
            current_route, route_num = queue.popleft()
            if end in route_stop_mapping[current_route]:
                return route_num
            for stop in route_stop_mapping[current_route]:
                for route in stop_route_mapping[stop]:
                    if route not in visited:
                        visited.add(route)
                        queue.append((route, route_num + 1))
        return -1
    
    def create_mappings(self, routes):
        route_stop_mapping = defaultdict(set)
        stop_route_mapping = defaultdict(list)
        for route_id, route in enumerate(routes):
            for stop in route:
                route_stop_mapping[route_id].add(stop)
                stop_route_mapping[stop].append(route_id)
        return route_stop_mapping, stop_route_mapping
    
    def find_initial_routes(self, start, stop_route_mapping):
        queue = deque()
        visited = set()
        for route in stop_route_mapping[start]:
            queue.append((route, 1))
            visited.add(route)
        return queue, visited
    
    