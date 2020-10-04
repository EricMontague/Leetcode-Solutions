"""This file contains my solutions to Leetcode problem 994: Rotting Oranges."""


# time complexity: O(mn), where 'm' is the number of rows and 'n' is the number of columns
# space complexity: O(mn), where 'm' is the number of rows and 'n' is the number of columns

class CellType:
    
    EMPTY = 0
    FRESH_ORANGE = 1
    ROTTEN_ORANGE = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        fresh_oranges, rotten_oranges = self.get_fresh_and_rotten_oranges(grid)
        return self.minimum_minutes_until_no_fresh_oranges(fresh_oranges, rotten_oranges, grid)
    
    def get_fresh_and_rotten_oranges(self, grid):
        fresh_oranges = set()
        rotten_oranges = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                orange = grid[row][col]
                if orange == CellType.ROTTEN_ORANGE:
                    rotten_oranges.add((row, col))
                elif orange == CellType.FRESH_ORANGE:
                    fresh_oranges.add((row, col))
        
        return fresh_oranges, rotten_oranges
    
    def minimum_minutes_until_no_fresh_oranges(self, fresh_oranges, rotten_oranges, grid):
        minutes = 0
        while fresh_oranges:
            infected_oranges = set()
            for rotten_orange in rotten_oranges:
                for neighbor_row, neighbor_col in self.get_neighbors(
                    rotten_orange[0], rotten_orange[1], grid
                ):
                    orange = (neighbor_row, neighbor_col)
                    if orange in fresh_oranges:
                        fresh_oranges.remove(orange)
                        infected_oranges.add(orange)
            if not infected_oranges:
                return -1
            rotten_oranges = infected_oranges
            minutes += 1
        return minutes
        
    
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
    
 

# time complexity: O(mn), where 'm' is the number of rows and 'n' is the number of columns
# space complexity: O(mn), where 'm' is the number of rows and 'n' is the number of columns

from collections import deque

class CellType:
    
    EMPTY = 0
    FRESH_ORANGE = 1
    ROTTEN_ORANGE = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        num_fresh_oranges, orange_queue = self.get_rotting_and_fresh_oranges(grid)
        return self.minimum_minutes_until_no_fresh_oranges(num_fresh_oranges, orange_queue, grid)
    
    def get_rotting_and_fresh_oranges(self, grid):
        num_fresh_oranges = 0
        orange_queue = deque()
        initial_time = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == CellType.ROTTEN_ORANGE:
                    orange_queue.append((row, col, initial_time))
                elif grid[row][col] == CellType.FRESH_ORANGE:
                    num_fresh_oranges += 1
        return num_fresh_oranges, orange_queue
    
    def minimum_minutes_until_no_fresh_oranges(self, num_fresh_oranges, orange_queue, grid):
        minimum_minutes = 0
        while orange_queue:
            row, col, minutes = orange_queue.popleft()
            minimum_minutes = max(minimum_minutes, minutes)
            for neighbor_row, neighbor_col in self.get_neighbors(row, col, grid):
                if grid[neighbor_row][neighbor_col] == CellType.FRESH_ORANGE:
                    orange_queue.append((neighbor_row, neighbor_col, minutes + 1))
                    grid[neighbor_row][neighbor_col] = CellType.ROTTEN_ORANGE
                    num_fresh_oranges -= 1
        if num_fresh_oranges > 0:
            return -1
        return minimum_minutes
    
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
    
    