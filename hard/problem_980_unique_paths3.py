"""This file contains my solutions to Leetcode problem 980: Unique Paths III."""



# Time complexity: O(3 ^ n), where 'n' is the number of cells that
# contain 0's.
# space complexity: O(n)

# Time and space analysis comes from here: https://leetcode.com/problems/unique-paths-iii/discuss/221941/C%2B%2B-brute-force-DFS
class CellType:
    
    OBSTACLE = -1
    EMPTY = 0
    START = 1
    END = 2
    
    
    
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        start, end, num_empty = self.setup(grid)
        return self.find_unique_paths(start, end, num_empty, grid, visited)
    
    def setup(self, grid):
        start = None
        end = None
        num_empty = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cell_value = grid[row][col]
                if cell_value == CellType.EMPTY:
                    num_empty += 1
                elif cell_value == CellType.START:
                    start = (row, col)
                elif cell_value == CellType.END:
                    end = (row, col)
        return start, end, num_empty
    
    def find_unique_paths(self, start, end, num_empty, grid, visited):
        if not self.is_valid_cell(start, grid):
            return 0
        if start in visited:
            return 0
        if start == end:
            if len(visited) - 1 == num_empty:
                return 1
            return 0
        visited.add(start)
        row, col = start
        num_paths = (
            self.find_unique_paths((row + 1, col), end, num_empty, grid, visited)
            + self.find_unique_paths((row -1, col), end, num_empty, grid, visited)
            + self.find_unique_paths((row, col + 1), end, num_empty, grid, visited)
            + self.find_unique_paths((row, col - 1), end, num_empty, grid, visited)
        )
        visited.remove(start)
        return num_paths
    
    def is_valid_cell(self, cell, grid):
        row, col = cell
        num_rows = len(grid)
        num_cols = len(grid[0])
        if (
            row >= num_rows
            or row < 0
            or col >= num_cols
            or col < 0
            or grid[row][col] == CellType.OBSTACLE
        ):
            return False
        return True