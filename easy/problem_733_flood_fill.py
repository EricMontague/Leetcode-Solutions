"""This file contains my solutions to Leetcode problem 733: Flood Fill."""


# time complexity: O(mn), where 'm' is the number of rows and 'n' is the number
# of cols
# space complexity: O(m + n)
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        if not image or image[sr][sc] == new_color:
            return image
        original_color = image[sr][sc]
        image[sr][sc] = new_color
        queue = deque([(sr, sc)])
        while queue:
            row, col = queue.popleft()
            for neighbor_row, neighbor_col in self.get_neighbors(
                image, row, col
            ):
                if image[neighbor_row][neighbor_col] == original_color:
                    image[neighbor_row][neighbor_col] = new_color
                    queue.append((neighbor_row, neighbor_col))
        return image
    
    def get_neighbors(self, image, row, col):
        num_rows = len(image)
        num_cols = len(image[0])
        for neighbor_row, neighbor_col in [
          (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)  
        ]:
            if (
                neighbor_row < num_rows
                and neighbor_row >= 0
                and neighbor_col < num_cols
                and neighbor_col >= 0
            ):
                yield neighbor_row, neighbor_col
        
        

# time complexity: O(mn), where 'm' is the number of rows and 'n' is the number
# of cols
# space complexity: O(mn)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        if not image or image[sr][sc] == new_color:
            return image
        original_color = image[sr][sc]
        self.fill_image(image, (sr, sc), original_color, new_color)
        return image
    
    def fill_image(self, image, cell, original_color, new_color):
        row, col = cell
        image[row][col] = new_color
        for neighbor_row, neighbor_col in self.get_neighbors(
            image, row, col
        ):
            if image[neighbor_row][neighbor_col] == original_color:
                self.fill_image(
                    image, 
                    (neighbor_row, neighbor_col),
                    original_color,
                    new_color
                )
    
    def get_neighbors(self, image, row, col):
        num_rows = len(image)
        num_cols = len(image[0])
        for neighbor_row, neighbor_col in [
          (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)  
        ]:
            if (
                neighbor_row < num_rows
                and neighbor_row >= 0
                and neighbor_col < num_cols
                and neighbor_col >= 0
            ):
                yield neighbor_row, neighbor_col
        
        