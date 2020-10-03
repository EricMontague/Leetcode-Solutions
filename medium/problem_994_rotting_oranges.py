"""This file contains my solutions to Leetcode problem 994: Rotting Oranges."""


from collections import deque

class CellType:
    
    EMPTY = 0
    FRESH_ORANGE = 1
    ROTTEN_ORANGE = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        orange_queue = self.get_rotting_oranges(grid)
        return self.minimum_minutes_until_no_fresh_oranges(orange_queue, grid)
    
    def get_rotting_oranges(self, grid):
        orange_queue = deque()
        initial_time = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == CellType.ROTTEN_ORANGE:
                    orange_queue.append((row, col, initial_time))
        return orange_queue
    
    def minimum_minutes_until_no_fresh_oranges(self, orange_queue, grid):
        minimum_minutes = 0
        while orange_queue:
            row, col, minutes = orange_queue.popleft()
            minimum_minutes = max(minimum_minutes, minutes)
            for neighbor_row, neighbor_col in self.get_neighbors(row, col, grid):
                if grid[neighbor_row][neighbor_col] == CellType.FRESH_ORANGE:
                    orange_queue.append((neighbor_row, neighbor_col, minutes + 1))
                    grid[neighbor_row][neighbor_col] = CellType.ROTTEN_ORANGE
        if not self.has_fresh_orange(grid):
            return minimum_minutes
        return -1
    
    def get_neighbors(self, row, col, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        for neighbor_row, neighbor_col in [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)
        ]:
            if (
                neighbor_row < num_rows
                and neighbor_row > -1
                and neighbor_col < num_cols
                and neighbor_col > -1
            ):
                yield neighbor_row, neighbor_col
    
    def has_fresh_orange(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == CellType.FRESH_ORANGE:
                    return True
        return False