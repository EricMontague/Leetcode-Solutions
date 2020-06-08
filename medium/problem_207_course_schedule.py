"""This is my solution to Leetcode problem 207: Course Schedule."""


#Overall time complexity: O(VE), where V is the number of vertices in the graph
# and E is the number of edges in the graph. If this were a complete graph, 
# then this could be O(V^3) because E = V ^2 in a complete graph

#Overall space complexity: O(V)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        dfsTree = set()
        for course in range(numCourses):
            if course not in visited:
                if self.hasCycle(visited, dfsTree, course, prerequisites):
                    return False
        return True
    
    def hasCycle(self, visited, dfsTree, course, prerequisites):
        visited.add(course)
        dfsTree.add(course)
        for nextCourse, prerequisite in prerequisites:
            if prerequisite == course:
                if nextCourse not in visited:
                    if self.hasCycle(visited, dfsTree, nextCourse, prerequisites):
                        return True
                elif nextCourse in dfsTree:
                    return True
        dfsTree.remove(course)
        return False
