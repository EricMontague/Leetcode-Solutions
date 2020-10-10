"""This is my solution to Leetcode problem 207: Course Schedule."""

# BFS Solution - Cycle Detection Algorithm
# Credit: https://leetcode.com/problems/course-schedule/discuss/58537/AC-Python-topological-sort-52-ms-solution-O(V-%2B-E)-time-and-O(V-%2B-E)-space

# time complexity: O(V + E), where 'V' is the number of prerequisite courses
# and E is the number of courses that have prerequisites

# space complexity: O(V + E)

from collections import defaultdict, deque


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        if num_courses == 0 or not prerequisites:
            return True

        # convert to adjacency list to make BFS more efficient
        prereq_adjacency_list = self.convert_edge_list_to_adjacency_list(prerequisites)

        # count in degree of each vertex
        prerequisite_counts = self.count_prerequisites(prerequisites, num_courses)

        # enqueue all vertices with an in degree of 0
        course_queue = self.get_starting_courses(prerequisite_counts)

        # Perform BFS. If you are able to visit all vertices in the graph,
        # then that means there are no cycles and you can take all courses
        return self.can_take_all_courses(
            prereq_adjacency_list, prerequisite_counts, course_queue
        )

    def convert_edge_list_to_adjacency_list(self, prerequisites):
        prereq_adjacency_list = defaultdict(list)
        for course, prerequisite in prerequisites:
            prereq_adjacency_list[prerequisite].append(course)
        return prereq_adjacency_list

    def count_prerequisites(self, prerequisite_edge_list, num_courses):
        prerequisite_counts = [0] * num_courses
        for course, prerequisite in prerequisite_edge_list:
            prerequisite_counts[course] += 1
        return prerequisite_counts

    def get_starting_courses(self, prerequisite_counts):
        course_queue = deque()
        for index, num_prereqs in enumerate(prerequisite_counts):
            if num_prereqs == 0:
                course_queue.append(index)
        return course_queue

    def can_take_all_courses(self, prereq_adjacency_list, prereq_counts, queue):
        num_courses_taken = 0
        while queue:
            taken_course = queue.popleft()
            num_courses_taken += 1
            for course in prereq_adjacency_list[taken_course]:
                prereq_counts[course] -= 1
                if prereq_counts[course] == 0:
                    queue.append(course)
        return num_courses_taken == len(prereq_adjacency_list)


# DFS Solution - Cycle Detection Algorithm
# Overall time complexity: O(V + E), where V is the number of vertices in the graph
# and E is the number of edges in the graph. If this were a complete graph,
# then this could be O(V^2) because E = V ^2 in a complete graph

# Overall space complexity: O(V + E)


class NodeState:

    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        if num_courses == 0 or not prerequisites:
            return True
        prereq_adjacency_list = self.convert_edge_list_to_adjacency_list(prerequisites)
        node_states = [NodeState.UNVISITED] * num_courses

        for course in range(num_courses):
            if node_states[course] == NodeState.UNVISITED:
                if not self.can_take_all_courses(
                    course, prereq_adjacency_list, node_states
                ):
                    return False
        return True

    def convert_edge_list_to_adjacency_list(self, prerequisites):
        prereq_adjacency_list = defaultdict(list)
        for course, prerequisite in prerequisites:
            prereq_adjacency_list[prerequisite].append(course)
        return prereq_adjacency_list

    def can_take_all_courses(self, prerequisite, prereq_adjacency_list, node_states):
        node_states[prerequisite] = NodeState.VISITING
        for course in prereq_adjacency_list[prerequisite]:
            if node_states[course] == NodeState.UNVISITED:
                if not self.can_take_all_courses(
                    course, prereq_adjacency_list, node_states
                ):
                    return False
            elif node_states[course] == NodeState.VISITING:
                return False
        node_states[prerequisite] = NodeState.VISITED
        return True


# Below is an iterative version of the method, can_take_call_courses()
# Writing an iterative version gives you the same time complexity
# as well as space complexity
def can_take_all_courses(self, course, prereq_adjacency_list, node_states):
        stack = [course]
        while stack:
            current_course = stack.pop()
            if node_states[current_course] == NodeState.UNVISITED:
                node_states[current_course] = NodeState.VISITING
                stack.append(current_course)
            elif node_states[current_course] == NodeState.VISITING:
                node_states[current_course] = NodeState.VISITED
            for next_course in prereq_adjacency_list[current_course]:
                if node_states[next_course] == NodeState.UNVISITED:
                    stack.append(next_course)
                elif node_states[next_course] == NodeState.VISITING:
                    return False
        return True
