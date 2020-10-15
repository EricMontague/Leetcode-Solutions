"""This file contains my solutino to Leetcode problem 990: Satisfiability of Equality Equations."""


# time complexity: O(n), where 'n' is the number of equations
# space complexity: O(1)
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
        if root_one != root_two:
            if self.ranks[root_one] < self.ranks[root_two]:
                self.parents[root_one] = root_two
            elif self.ranks[root_two] < self.ranks[root_one]:
                self.parents[root_two] = root_one
            else:
                self.parents[root_one] = root_two
                self.ranks[root_two] += 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind(26)
        for equation in equations:
            if equation[1] == "=":
                element_one = ord(equation[0]) - ord("a")
                element_two = ord(equation[3]) - ord("a")
                union_find.union(element_one, element_two)
        return self.are_equations_possible(equations, union_find)
     
    def are_equations_possible(self, equations, union_find):
        for equation in equations:
            if equation[1] == "!":
                element_one = ord(equation[0]) - ord("a")
                element_two = ord(equation[3]) - ord("a")
                if (
                    union_find.find(element_one) 
                    == union_find.find(element_two)
                ):
                    return False
        return True



# Recursive DFS Solution
# time complexity: O(n), where 'n' is the number of equations
# space complexity: O(1)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        adjacency_list = self.build_adjacency_list(equations)
        components = self.find_connected_components(adjacency_list)
        return self.are_equations_possible(equations, components)
        
    def build_adjacency_list(self, equations):
        adjacency_list = {}
        for equation in equations:
            char_one = equation[0]
            char_two = equation[3]
            adjacency_list.setdefault(char_one, [])
            adjacency_list.setdefault(char_two, [])
            if equation[1] == "=":    
                adjacency_list[char_one].append(char_two)
                adjacency_list[char_two].append(char_one)
        return adjacency_list
        
    def find_connected_components(self, adjacency_list):
        components = []
        for node in adjacency_list:
            component = set()
            if node not in component:
                self.build_component(node, adjacency_list, component)
                components.append(component)
        return components
    
    def build_component(self, node, adjacency_list, component):
        component.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor not in component:
                self.build_component(neighbor, adjacency_list, component)
         
     
    def are_equations_possible(self, equations, components):
        for equation in equations:
            if equation[1] == "!":
                for component in components:
                    if equation[0] in component and equation[3] in component:
                        return False
        return True