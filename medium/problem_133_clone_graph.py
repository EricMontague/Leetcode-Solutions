"""This file contains my solution to Leetcode problem 133: Clone Graph."""



# Recursive DFS Solution

# time complexity: O(V + E), where 'V' is the number of vertices
# and 'E' is the number of edges

# space complexity: O(V)

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clones = {}
        return self.copy_graph(node, clones)
    
    def copy_graph(self, current_node, clones):
        if current_node is None:
            return current_node
        new_node = Node(current_node.val, [])
        clones[current_node.val] = new_node
        for neighbor in current_node.neighbors:
            if neighbor.val not in clones:
                child_copy = self.copy_graph(neighbor, clones)    
            new_node.neighbors.append(clones[neighbor.val])
        return new_node


# Iterative DFS Solution

class Solution:
    def cloneGraph(self, source: 'Node') -> 'Node':
        if source is None:
            return source
        visited = {}
        new_source = Node(source.val, [])
        visited[source.val] = new_source
        stack = [source]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val, [])
                    stack.append(neighbor)
                visited[node.val].neighbors.append(visited[neighbor.val])
        return new_source


# BFS Solution
# time complexity: O(V + E), where 'V' is the number of vertices
# and 'E' is the number of edges

# space complexity: O(V)

from collections import deque

class Solution:
    def cloneGraph(self, source: 'Node') -> 'Node':
        if source is None:
            return source
        clones = {}
        new_source = Node(source.val, [])
        clones[source.val] = new_source
        queue = deque([source])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clones[node.val].neighbors.append(clones[neighbor.val])
        return new_source