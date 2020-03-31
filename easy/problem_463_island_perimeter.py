"""This is my solution to Leetcode problem 463."""



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(grid[row_index]):
                if value == 1:
                    shared_sides = self.count_shared_sides(row_index, col_index, grid)
                    perimeter += (4 - shared_sides)
        return perimeter
    
    def count_shared_sides(self, row, col, grid):
        shared_sides = 0
        for num_row, num_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if num_row > - 1 and num_row < len(grid) and num_col > - 1 and num_col < len(grid[0]):
                if grid[num_row][num_col] == 1:
                    shared_sides += 1
        return shared_sides
                    
        
#Overall time complexity: O(N ^ 2), where "N" is the number of rows and columns
#Explanation: You have to iterate over all "N" rows and "N" columns in the matrix in
#order to calculate the perimeter. During the iteration on the columns, this makes a
#call to count_shared_sides(), but this method contains a loop that runs exact 4 times
#regardless of the size of input. So, this would make the time complexity O(4N^2), but
#after dropping the coefficient, this just becomes O(N^2)


#Oversall space complexity: O(1)
#Explanation: No matter how that size of the input grid changes, the amount of space
#used remains constant. Space is consumed by the two variables and the list in the helper method,
#but the same two variables and same sized list are used regardless of how the grid size changes.
