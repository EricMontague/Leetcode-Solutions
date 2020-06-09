"""This is my solution to Leetcode problem 207: Course Schedule."""


#Overall time complexity: O(V + E), where V is the number of vertices in the graph
# and E is the number of edges in the graph. If this were a complete graph, 
# then this could be O(V^2) because E = V ^2 in a complete graph

#Overall space complexity: O(V)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        dfsTree = set()
        adjacency_list = self.buildAdjList(numCourses, prerequisites)
        for course in range(numCourses):
            if course not in visited:
                if self.hasCycle(visited, dfsTree, course, adjacency_list):
                    return False
        return True
    
    def buildAdjList(self, numCourses, prerequisites):
        adjacency_list = [[] for course in range(numCourses)]
        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
        return adjacency_list
    
    def hasCycle(self, visited, dfsTree, course, prerequisites):
        visited.add(course)
        dfsTree.add(course)
        for nextCourse in prerequisites[course]:
            if nextCourse not in visited:
                if self.hasCycle(visited, dfsTree, nextCourse, prerequisites):
                    return True
            elif nextCourse in dfsTree:
                return True
        dfsTree.remove(course)
        return False