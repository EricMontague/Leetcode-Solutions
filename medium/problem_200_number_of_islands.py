"""This contains my solutions to Leetcode problem 200."""

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
class UnionFind:
    
    def __init__(self, size):
        self.parents = [0] * size
        self.ranks = [0] * size
        self.size = size
        self.num_components = 0
        self.make_set()
        
    def make_set(self):
        for index in range(self.size):
            self.parents[index] = index
        
    def find(self, element):
        root = element
        while self.parents[root] != root:
            root = self.parents[root]
        
        #path compression
        while self.parents[element] != root:
            parent = self.parents[element]
            self.parents[element] = root
            element = parent
        return root
    
    def union(self, element_one, element_two):
        root_one = self.find(element_one)
        root_two = self.find(element_two)
        
        if root_one != root_two:
            if self.ranks[root_one] > self.ranks[root_two]:
                self.parents[root_two] = root_one
            elif self.ranks[root_one] < self.ranks[root_two]:
                self.parents[root_one] = root_two
            elif self.ranks[root_one] == self.ranks[root_two]:
                self.parents[root_one] = root_two
                self.ranks[root_two] += 1
            self.num_components -= 1



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row_count = len(grid)
        col_count = len(grid[0])
        union_find = UnionFind(row_count * col_count)
        self.merge_sets(union_find, grid, row_count, col_count)
        return union_find.num_components
        
    def merge_sets(self, union_find, grid, row_count, col_count):
        for row_index in range(row_count):
            for col_index in range(col_count):
                    if grid[row_index][col_index] == "1":
                        union_find.num_components += 1
                        for num_row, num_col in self.get_neighbors(row_index, col_index, grid):
                            if grid[num_row][num_col] == "1":
                                element_one = row_index * col_count + col_index
                                element_two = num_row * col_count + num_col
                                union_find.union(element_one, element_two)
                    
    def get_neighbors(self, row, col, grid):
        for num_row, num_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if num_row > - 1 and num_row < len(grid) and num_col > - 1 and num_col < len(grid[0]):
                yield num_row, num_col
                
