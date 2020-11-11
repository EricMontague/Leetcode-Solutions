"""This file contains my solutions to Leetcode problem 63: Unique Paths 2."""


# Bottom Up Solution more space efficient
# time complexity: O(mn), where 'm' is the number of rows and 'n'
# is the number of columns
# space complexity: O(m)

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        if grid[num_rows - 1][num_cols - 1] == 1:
            return 0
        num_paths = [0] * num_cols
        num_paths[-1] = 1
        for row in range(num_rows -1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                if grid[row][col] == 1:
                    num_paths[col] = 0
                elif col < num_cols - 1:
                    num_paths[col] += num_paths[col + 1]
        return num_paths[0]
    
  

# Bottom Up Solution
# time complexity: O(mn), where 'm' is the number of rows and 'n'
# is the number of columns
# space complexity: O(mn)
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        if grid[num_rows - 1][num_cols - 1] == 1:
            return 0
        num_paths = [[-1] * num_cols for row in range(num_rows)]
        for row in range(num_rows - 1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                # Base case
                if row == num_rows - 1 and col == num_cols - 1:
                    num_paths[row][col] = 1
                # Obstacle
                elif grid[row][col] == 1:
                    num_paths[row][col] = 0
                # Last row
                elif row == num_rows - 1:
                    num_paths[row][col] = num_paths[row][col + 1]
                # Last column
                elif col == num_cols - 1:
                    num_paths[row][col] = num_paths[row + 1][col]
                else:
                    num_paths[row][col] = (
                        num_paths[row + 1][col]
                        + num_paths[row][col + 1]
                    )
        return num_paths[0][0]


# time complexity: O(mn), where 'm' is the number of rows and 'n'
# is the number of columns
# space complexity: O(mn)
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_paths = [[-1] * num_cols for row in range(num_rows)]
        return self.count_unique_paths(
            (0, 0),
            (num_rows - 1, num_cols - 1),
            grid,
            num_paths
        )
    
    def count_unique_paths(self, current, dest, grid, num_paths):
        if not self.is_valid_cell(current, grid):
            return 0
        row, col = current
        if num_paths[row][col] >= 0:
            return num_paths[row][col]
        if grid[row][col] == 1:
            paths = 0
        elif current == dest:
            paths = 1
        else:
            paths = (
                self.count_unique_paths((row + 1, col), dest, grid, num_paths)
                + self.count_unique_paths((row, col + 1), dest, grid, num_paths)
            )
        num_paths[row][col] = paths
        return paths
        
    def is_valid_cell(self, current_cell, grid):
        row, col = current_cell
        num_rows = len(grid)
        num_cols = len(grid[0])
        if (
            row >= num_rows
            or row < 0
            or col >= num_cols
            or col < 0
        ):
            return False
        return True