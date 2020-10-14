"""This file contains my solutions to Leetcode problem 785: Is Graph Bipartite.?"""

# Union Find Solution
# Time complexity: O(V + E), where 'V' is the number of vertices and 'E' is 
# the number of edges
# space complexity: O(V)
from collections import defaultdict

class UnionFind:
    
    def __init__(self, size):
        self.size = size
        self.parents = [-1] * size
        self.ranks = [0] * size
        self.make_set()
        
    def make_set(self):
        for i in range(self.size):
            self.parents[i] = i
    
    def find(self, element):
        if self.parents[element] == element:
            return element
        root = self.find(self.parents[element])
        self.parents[element] = root
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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        union_find = UnionFind(len(graph))
        
        for node in range(len(graph)):
            for neighbor in graph[node]:
                if union_find.find(node) == union_find.find(neighbor):
                    return False
                union_find.union(graph[node][0], neighbor)
        return True
                

# BFS Solution
# Time complexity: O(V + E), where 'V' is the number of vertices and 'E' is 
# the number of edges
# space complexity: O(V)

from collections import deque

class Color:
    RED = 0
    YELLOW = 1
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        colors = [None] * len(graph)
        for node in range(len(graph)):
            if colors[node] is None:
                if not self.is_two_colorable(node, graph, colors):
                    return False
        return True
    
    def is_two_colorable(self, source, graph, colors):
        colors[source] = Color.RED
        queue = deque([source])
        while queue:
            current_node = queue.popleft()
            for neighbor in graph[current_node]:
                if colors[neighbor] is None:
                    color = self.assign_color(current_node, colors)
                    colors[neighbor] = color
                    queue.append(neighbor)
                else:
                    if colors[neighbor] == colors[current_node]:
                        return False
        return True
    
    def assign_color(self, current_node, colors):
        if colors[current_node] == Color.RED:
            return Color.YELLOW
        return Color.RED



# Recursive DFS Solution
# Time complexity: O(V + E), where 'V' is the number of vertices and 'E' is 
# the number of edges
# space complexity: O(V)
#  
class Color:
    RED = 0
    YELLOW = 1
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        colors = [None] * len(graph)
        for node in range(len(graph)):
            if colors[node] is None:
                colors[node] = Color.RED
                if not self.is_two_colorable(node, graph, colors):
                    return False
        return True
    
    def is_two_colorable(self, current_node, graph, colors):
        for neighbor in graph[current_node]:
            if colors[neighbor] is None:
                color = self.assign_color(current_node, colors)
                colors[neighbor] = color
                if not self.is_two_colorable(neighbor, graph, colors):
                    return False
            else:
                if colors[neighbor] == colors[current_node]:
                    return False
        return True
    
    def assign_color(self, current_node, colors):
        if colors[current_node] == Color.RED:
            return Color.YELLOW
        return Color.RED
    
        


# Iterative DFS Solution
# Time complexity: O(V + E), where 'V' is the number of vertices and 'E' is 
# the number of edges
# space complexity: O(V)     
class Color:
    RED = 0
    YELLOW = 1
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        colors = [None] * len(graph)
        for node in range(len(graph)):
            if colors[node] is None:
                colors[node] = Color.RED
                if not self.is_two_colorable(node, graph, colors):
                    return False
        return True
    
    def is_two_colorable(self, source, graph, colors):
        stack = [source]
        while stack:
            current_node = stack.pop()
            for neighbor in graph[current_node]:
                if colors[neighbor] is None:
                    color = self.assign_color(current_node, colors)
                    colors[neighbor] = color
                    stack.append(neighbor)
                else:
                    if colors[neighbor] == colors[current_node]:
                        return False
        return True
    
    def assign_color(self, current_node, colors):
        if colors[current_node] == Color.RED:
            return Color.YELLOW
        return Color.RED
    
        
        
                