"""This contains my solutions to Leetcode problem 200."""


# BFS Solution
# time complexity:
# space complexity: O(max(n, m))
from collections import deque

class CellType:
    
    WATER = "0"
    LAND = "1"
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        if not grid:
            return num_islands
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[False] * num_cols for row in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == CellType.LAND and not visited[row][col]:
                    num_islands += 1
                    self.explore_island(row, col, grid, visited)
        return num_islands
    
    def explore_island(self, row, col, grid, visited):
        visited[row][col] = True
        queue = deque([(row, col)])
        while queue:
            current_row, current_col = queue.popleft()
            for neighbor_row, neighbor_col in self.get_neighbors(
                current_row, current_col, grid
            ):
                if not visited[neighbor_row][neighbor_col]:
                    visited[neighbor_row][neighbor_col] = True
                    queue.append((neighbor_row, neighbor_col))
    
    def get_neighbors(self, row, col, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        for neighbor_row, neighbor_col in [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]:
            if (
                neighbor_row < num_rows
                and neighbor_row > -1
                and neighbor_col < num_cols
                and neighbor_col > - 1
                and grid[neighbor_row][neighbor_col] == CellType.LAND
            ):
                yield neighbor_row, neighbor_col

#Overall time complexity: O(nm + k), where "n" is the number of rows, "m" is the number
#of columns, and "k" is the total number of patches of land ("1" 's) in the grid
#Overall space complexity: O(nm)
class CellType:
    
    WATER = "0"
    LAND = "1"
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        if not grid:
            return number_of_islands
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[False] * num_cols for row in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == CellType.LAND and not visited[row][col]:
                    number_of_islands += 1
                    self.explore_island(row, col, grid, visited)
        return number_of_islands
    
    def explore_island(self, row, col, grid, visited):
        if self.is_valid_cell(row, col, grid, visited):
            visited[row][col] = True
            self.explore_island(row + 1, col, grid, visited)
            self.explore_island(row - 1, col, grid, visited)
            self.explore_island(row, col + 1, grid, visited)
            self.explore_island(row, col - 1, grid, visited)
    
    def is_valid_cell(self, row, col, grid, visited):
        num_rows = len(grid)
        num_cols = len(grid[0])
        if (
            row < num_rows
            and row > -1
            and col < num_cols
            and col > -1
            and grid[row][col] == CellType.LAND
            and not visited[row][col]
        ):
            return True
        return False


#Alternative Depth First Search method
#Overall time complexity of solution with iterative DFS is O(nm + k) still
#Overall space complexity of solution with ierative DFS is O(n + m), meaning that
#the maximum space taken up on the stack is dependent on which is greater, the number of 
#rows, or the number of columns.
class CellType:
    
    WATER = "0"
    LAND = "1"
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        if not grid:
            return number_of_islands
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[False] * num_cols for row in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == CellType.LAND and not visited[row][col]:
                    number_of_islands += 1
                    self.explore_island(row, col, grid, visited)
        return number_of_islands
    
    def explore_island(self, row, col, grid, visited):
        stack = [(row, col)]
        while stack:
            current_row, current_col = stack.pop()
            for neighbor_row, neighbor_col in self.get_neighbors(
                current_row, current_col, grid
            ):
                if (
                    not visited[neighbor_row][neighbor_col]
                    and grid[neighbor_row][neighbor_col] == CellType.LAND
                ):
                    visited[neighbor_row][neighbor_col] = True
                    stack.append((neighbor_row, neighbor_col))
                    
    
    def get_neighbors(self, row, col, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        for neighbor_row, neighbor_col in [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]:
            if (
                neighbor_row < num_rows
                and neighbor_row > -1
                and neighbor_col < num_cols
                and neighbor_col > -1
            ):
                yield (neighbor_row, neighbor_col)
        



#Union find solution
#Overall time complexity: O(nm * alpha), where alpha is a slow growing
#constant equal to the inverse Ackermann function
#Overall space complexity: O(nm)
class CellType:
    
    WATER = "0"
    LAND = "1"
    

class UnionFind:
    
    def __init__(self, size, num_components):
        self.parents = [None] * size
        self.ranks = [0] * size
        self.size = size
        self.num_components = num_components
        self.make_set()
    
    def make_set(self):
        for index in range(len(self.parents)):
            self.parents[index] = index
        
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
        self.num_components -= 1
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_land_patches = self.count_num_land_patches(grid, num_rows, num_cols)
        union_find = UnionFind(num_rows * num_cols, num_land_patches)
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == CellType.LAND:
                    for neighbor_row, neighbor_col in self.get_neighbors(
                        row, col, grid
                    ):
                        element_one = num_cols * row + col
                        element_two = num_cols * neighbor_row + neighbor_col
                        union_find.union(element_one, element_two)    
        return union_find.num_components

    def count_num_land_patches(self, grid, num_rows, num_cols):
        num_land_patches = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == CellType.LAND:
                    num_land_patches += 1
        return num_land_patches
        
    def get_neighbors(self, row, col, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        for neighbor_row, neighbor_col in [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]:
            if (
                neighbor_row < num_rows
                and neighbor_row > -1
                and neighbor_col < num_cols
                and neighbor_col > -1
                and grid[neighbor_row][neighbor_col] == CellType.LAND
            ):
                yield (neighbor_row, neighbor_col)
        



        