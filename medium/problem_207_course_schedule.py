"""This is my solution to Leetcode problem 207: Course Schedule."""


#Overall time complexity: O(V + E), where V is the number of vertices in the graph
# and E is the number of edges in the graph. If this were a complete graph, 
# then this could be O(V^2) because E = V ^2 in a complete graph

#Overall space complexity: O(V + E)


#Enumeration class used for graph coloring
class State:
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        states = [0] * numCourses
        adjacency_list = self.buildAdjList(numCourses, prerequisites)
        for course in range(numCourses):
            if states[course] == State.UNVISITED:
                if self.hasCycle(states, course, adjacency_list):
                    return False
        return True
    
    def buildAdjList(self, numCourses, prerequisites):
        adjacency_list = [[] for course in range(numCourses)]
        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
        return adjacency_list
    
    def hasCycle(self, states, course, prerequisites):
        states[course] = State.VISITING
        for nextCourse in prerequisites[course]:
            if states[nextCourse] == State.UNVISITED:
                if self.hasCycle(states, nextCourse, prerequisites):
                    return True
            if states[nextCourse] == State.VISITING:
                return True
        states[course] = State.VISITED
        return False



# Below is an iterative version of the method, hasCycle
# Writing an iterative version gives you the same time complexity
# as well as space complexity
def hasCycle(states, course, prerequisites):
    stack = []
    stack.append((course, False))
    states[course] = State.VISITING
    while stack:
        currentCourse, finished = stack.pop()
        if finished:
            states[currentCourse] = State.VISITED
        else:
            stack.append((currentCourse, True))
            for nextCourse in prerequisites[currentCourse]:
                if states[nextCourse] == State.UNVISITED:
                    stack.append((nextCourse, False))
                    states[currentCourse] = State.VISITING
                if states[nextCourse] == State.VISITING:
                    return True
    return False