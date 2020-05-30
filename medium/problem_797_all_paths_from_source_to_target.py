"""This script contains my solution to Leetcode problem 706."""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sourceNode = 0
        allPaths = []
        currentPath = []
        if not graph:
            return allPaths
        currentPath.append(sourceNode)
        self.findAllPaths(graph, allPaths, currentPath, sourceNode)
        return allPaths
    
    def findAllPaths(self, graph, allPaths, currentPath, currentNode):
        if currentNode == len(graph) - 1:
            allPaths.append(currentPath[:])
        else:
            for neighbor in graph[currentNode]:
                currentPath.append(neighbor)
                self.findAllPaths(graph, allPaths, currentPath, neighbor)
                currentPath.pop()

                