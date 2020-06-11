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





# Another solution that uses BFS
# Overall time complexity: O(V + E)
# Overall space complexity: O(V + E)
# Credit: https://leetcode.com/problems/course-schedule/discuss/58537/AC-Python-topological-sort-52-ms-solution-O(V-%2B-E)-time-and-O(V-%2B-E)-space
from collections import deque


class Solution:
    def canFinish(self, numNodes, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        visited = set()
        graph, inDegrees = self.buildGraph(numNodes, edges)
        queue = self.buildQueue(inDegrees)
        self.bfs(queue, visited, inDegrees, graph)
        return len(visited) == numNodes
    
    def buildGraph(self, numNodes, edges):
        # construct graph
        
        # key represents a prerequisites
        # value is a set that represents the courses that come after that prereq
        graph = {node: set() for node in range(numNodes)} #outDegrees
        
        #key represents a course
        #value represents the number of prerequisites needed to take a course
        inDegrees = {node:0 for node in range(numNodes)}
        for edge in edges:
            graph[edge[1]].add(edge[0])
            inDegrees[edge[0]] += 1
        return graph, inDegrees
    
    def buildQueue(self, inDegrees):
        # find nodes whose out degree == 0
        # This represents finding all classes which don't have any
        # prerequisites
        queue = deque()
        for node, inDegree in inDegrees.items():
            if inDegree == 0:
                queue.append(node)
        return queue
    
    def bfs(self, queue, visited, inDegrees, graph):
        # loop all nodes whose out degree == 0
        
        # adding a node to the queue represents scheduling a course, which may
        # also be a prerequisite to other courses
        # while adding to it visited is marking it as taken
        # afterwards you decrement the number of prereqs needed
        # to take each course that is a neighbor of that prereq in the graph
        # if there are no more prereqs left to take, then you add that class(node)
        # to the queue (schedule it)
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)
        