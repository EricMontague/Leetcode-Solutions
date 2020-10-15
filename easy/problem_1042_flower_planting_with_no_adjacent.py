"""This file contains my solution to Leetcode problem 1042: Flower Planting With No Adjacenct."""


# time complexity: O(|V| + |E|), where 'V' is the number of vertices and 'E' is the number
# of edges
# space complexity: O(|V| + |E|)
class Color:
    NO_COLOR = 0
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4


class Solution:
    def gardenNoAdj(self, num_nodes: int, paths: List[List[int]]) -> List[int]:
        available_colors = [
            Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN
        ]
        assigned_colors = [Color.NO_COLOR] * num_nodes
        garden_adjacency_list = self.convert_edge_list_to_adjacency_list(
            paths, num_nodes
        )
        for node in range(1, num_nodes + 1):
            adjacent_colors = set()
            for neighbor in garden_adjacency_list[node]:
                if assigned_colors[neighbor - 1] != Color.NO_COLOR:
                    adjacent_colors.add(assigned_colors[neighbor - 1])
            for color in available_colors:
                if color not in adjacent_colors:
                    assigned_colors[node - 1] = color
                    break
        return assigned_colors
    
    def convert_edge_list_to_adjacency_list(self, edge_list, num_nodes):
        adjacency_list = {}
        for node in range(1, num_nodes + 1):
            adjacency_list[node] = []
        for start, end in edge_list:
            adjacency_list[start].append(end)
            adjacency_list[end].append(start)
        return adjacency_list
    
   