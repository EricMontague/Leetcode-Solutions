"""This file contains my solutions to Leetcode problem 79: Word Search."""


class Solution:

    VISITED = "#"

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.word_exists(row, col, board, word, 0):
                        return True
        return False

    def word_exists(self, current_row, current_col, board, word, index):
        if index == len(word) - 1:
            return True
        current_character = board[current_row][current_col]
        board[current_row][current_col] = self.VISITED
        for neighbor_row, neighbor_col in self.get_neighbors(
            current_row, current_col, board
        ):
            neighbor = board[neighbor_row][neighbor_col]
            if neighbor != self.VISITED and neighbor == word[index + 1]:
                if self.word_exists(neighbor_row, neighbor_col, board, word, index + 1):
                    return True
        board[current_row][current_col] = current_character
        return False

    def get_neighbors(self, current_row, current_col, board):
        num_rows = len(board)
        num_cols = len(board[current_row])
        for neighbor_row, neighbor_col in [
            (current_row + 1, current_col),
            (current_row - 1, current_col),
            (current_row, current_col + 1),
            (current_row, current_col - 1),
        ]:
            if (
                neighbor_row < num_rows
                and neighbor_row > -1
                and neighbor_col < num_cols
                and neighbor_col > -1
            ):
                yield (neighbor_row, neighbor_col)



# Alternative structure for the word_exists() method. Same complexities
class Solution:
    
    VISITED = "#"
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.word_exists(row, col, board, word, 0):
                        return True
        return False
    
    def word_exists(self, current_row, current_col, board, word, index):
        if not self.is_valid_cell(current_row, current_col, board, word[index]):
            return False
        if index == len(word) - 1:
            return True
        current_character = board[current_row][current_col]
        board[current_row][current_col] = self.VISITED
         
        if (
            self.word_exists(current_row + 1, current_col, board, word, index + 1)
            or self.word_exists(current_row -1, current_col, board, word, index + 1)
            or self.word_exists(current_row, current_col + 1, board, word, index + 1)
            or self.word_exists(current_row , current_col - 1, board, word, index + 1)
        ):
            return True
        
        board[current_row][current_col] = current_character
        return False
    
    def is_valid_cell(self, current_row, current_col, board, expected_character):
        num_rows = len(board)
        num_cols = len(board[0])
        if (
            current_row >= num_rows 
            or current_row < 0 
            or current_col >= num_cols 
            or current_col < 0
            or board[current_row][current_col] == self.VISITED
            or board[current_row][current_col] != expected_character
        ):
            return False
        return True