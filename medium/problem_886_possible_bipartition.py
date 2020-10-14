"""This file contains my solutions to Leetcode problem 886: Possible Bipartition."""


# BFS Solution
# time complexity - O(|V| + |E|), where 'V' is the number of vertices and 'E' is the number of edges
# space complexity: O(|V| + |E|)

from collections import deque, defaultdict


class Color:
    NO_COLOR = 0
    RED = 1
    YELLOW = 2

class Solution:
    def possibleBipartition(self, num_friends: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        dislikes_adjacency_list = self.convert_edge_list_to_adjacency_list(dislikes)
        colors = [Color.NO_COLOR] * num_friends
        for friend in range(1, num_friends + 1):
            if colors[friend - 1] == Color.NO_COLOR:
                colors[friend - 1] = Color.RED
                if not self.is_two_colorable(friend, dislikes_adjacency_list, colors):
                    return False
        return True
    
    def convert_edge_list_to_adjacency_list(self, edge_list):
        adjacency_list = defaultdict(list)
        for node_one, node_two in edge_list:
            adjacency_list[node_one].append(node_two)
            adjacency_list[node_two].append(node_one)
        return adjacency_list
    
    def is_two_colorable(self, source, adjacency_list, colors):
        queue = deque([source])
        while queue:
            current_node = queue.popleft()
            for neighbor in adjacency_list[current_node]:
                if colors[neighbor - 1] == Color.NO_COLOR:
                    colors[neighbor - 1] = self.assign_color(current_node, colors)
                    queue.append(neighbor)
                else:
                    if colors[neighbor - 1] == colors[current_node - 1]:
                        return False
        return True
    
    def assign_color(self, current_node, colors):
        if colors[current_node - 1] == Color.RED:
            return Color.YELLOW
        return Color.RED




# Recursive DFS Solution
# time complexity - O(|V| + |E|), where 'V' is the number of vertices and 'E' is the number of edges
# space complexity: O(|V| + |E|)
from collections import  defaultdict


class Color:
    NO_COLOR = 0
    RED = 1
    YELLOW = 2

class Solution:
    def possibleBipartition(self, num_friends: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        dislikes_adjacency_list = self.convert_edge_list_to_adjacency_list(dislikes)
        colors = [Color.NO_COLOR] * num_friends
        for friend in range(1, num_friends + 1):
            if colors[friend - 1] == Color.NO_COLOR:
                colors[friend - 1] = Color.RED
                if not self.is_two_colorable(friend, dislikes_adjacency_list, colors):
                    return False
        return True
    
    def convert_edge_list_to_adjacency_list(self, edge_list):
        adjacency_list = defaultdict(list)
        for node_one, node_two in edge_list:
            adjacency_list[node_one].append(node_two)
            adjacency_list[node_two].append(node_one)
        return adjacency_list
    
    def is_two_colorable(self, current_node, adjacency_list, colors):
        for neighbor in adjacency_list[current_node]:
            if colors[neighbor - 1] == Color.NO_COLOR:
                colors[neighbor - 1] = self.assign_color(current_node, colors)
                if not self.is_two_colorable(neighbor, adjacency_list, colors):
                    return False
            else:
                if colors[neighbor - 1] == colors[current_node - 1]:
                    return False
        return True
    
    
    def assign_color(self, current_node, colors):
        if colors[current_node - 1] == Color.RED:
            return Color.YELLOW
        return Color.RED

    
# Iterative implementation of is_two_colorable() for DFS
def is_two_colorable(self, source, adjacency_list, colors):
    stack = [source]
    while stack:
        current_node = stack.pop()
        for neighbor in adjacency_list[current_node]:
            if colors[neighbor - 1] == Color.NO_COLOR:
                colors[neighbor - 1] = self.assign_color(current_node, colors)
                stack.append(neighbor)
            else:
                if colors[neighbor - 1] == colors[current_node - 1]:
                    return False
    return True



# UnionFind solution
# time complexity - O(|V| + |E|), where 'V' is the number of vertices and 'E' is the number of edges
# space complexity: O(|V| + |E|)

class UnionFind:
    
    def __init__(self, size):
        self.parents = [index for index in range(size)]
        self.ranks = [0] * size
                
    def find(self, element):
        root = element
        while self.parents[root] != root:
            root = self.parents[root]
        
        current = element
        while self.parents[current] != current:
            parent = self.parents[current]
            self.parents[current] = root
            current = parent
        return root
    
    def union(self, element_one, element_two):
        root_one = self.find(element_one)
        root_two = self.find(element_two)
        if root_one == root_two:
            return
        if self.ranks[root_one] < self.ranks[root_two]:
            self.parents[root_one] = root_two
        elif self.ranks[root_two] < self.ranks[root_one]:
            self.parents[root_two] = root_one
        else:
            self.parents[root_one] = root_two
            self.ranks[root_two] += 1

class Solution:
    def possibleBipartition(self, num_friends: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        dislikes_adjacency_list = self.convert_edge_list_to_adjacency_list(dislikes)
        union_find = UnionFind(num_friends)
        for friend in range(1, num_friends + 1):
            for disliked_friend in dislikes_adjacency_list[friend]:
                if union_find.find(friend - 1) == union_find.find(disliked_friend - 1):
                    return False
                union_find.union(
                    dislikes_adjacency_list[friend][0] - 1,
                    disliked_friend - 1
                )
        return True
    
    def convert_edge_list_to_adjacency_list(self, edge_list):
        adjacency_list = defaultdict(list)
        for node_one, node_two in edge_list:
            adjacency_list[node_one].append(node_two)
            adjacency_list[node_two].append(node_one)
        return adjacency_list
    
 