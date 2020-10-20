"""This file contains my solutions to leetcode problem 62: Unique Paths."""


# Top down Solution

# time complexity: O(m * n), where 'm' is the number of rows and 'n' is the
# number of columns

# space complexity: O(m * n) - The recursive method's space complexity is O(m + n),
# but O(m * n) is a faster growing term
class Solution:
    def uniquePaths(self, num_rows: int, num_cols: int) -> int:
        # build memoization table
        memo = [[None] * num_cols for row in range(num_rows)]

        # initialize start and endpoints
        robot = (0, 0)
        destination = (num_rows - 1, num_cols - 1)
        return self.find_num_unique_paths(num_rows, num_cols, robot, destination, memo)
    
    def find_num_unique_paths(self, num_rows, num_cols, robot, destination, memo):
        # No matrix or invalid matrix
        if num_rows == 0 or num_cols == 0:
            return 0
        
        # extract cells
        current_row = robot[0]
        current_col = robot[1]
        
        # Out of bounds
        if current_row >= num_rows or current_col >= num_cols:
            return 0
        
        # Return cached value
        if memo[current_row][current_col] is not None:
            return memo[current_row][current_col]
        
        # Base case
        if robot == destination:
            memo[current_row][current_col] = 1
            return memo[current_row][current_col]
        
        # Recursive case
        num_paths =  (
            self.find_num_unique_paths(num_rows, num_cols, (current_row + 1, current_col), destination, memo)
            + self.find_num_unique_paths(num_rows, num_cols, (current_row, current_col + 1), destination, memo)
        )
        memo[current_row][current_col] = num_paths
        return memo[current_row][current_col]
        

# Bottom Up Solution
# time complexity: O(m * n), where 'm' is the number of rows and 'n' is the
# number of columns

# space complexity: O(m * n)

class Solution:
    def uniquePaths(self, num_rows: int, num_cols: int) -> int:
        if num_rows == 0 or num_cols == 0:
            return 0
        memo = [[None] * num_cols for row in range(num_rows)]
        start_row = 0
        start_col = 0
        for row in range(num_rows - 1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                # Base case
                if row == num_rows - 1 and col == num_cols - 1:
                    memo[row][col] = 1
                else:
                    unique_paths_down = 0
                    unique_paths_right = 0
                    if row + 1 < num_rows:
                        unique_paths_down = memo[row + 1][col]
                    if col + 1 < num_cols:
                        unique_paths_right = memo[row][col + 1]
                    memo[row][col] = unique_paths_down + unique_paths_right
        return memo[start_row][start_col]
    