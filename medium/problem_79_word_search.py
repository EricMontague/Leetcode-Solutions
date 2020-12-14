"""This file contains my solutions to Leetcode problem 79: Word Search."""


# time complexity: O(mn * 4^k), where 'm' is the number of rows, 'n' is the number
# of columns and 'k' is the length of the word
# space complexity: O(nm)


# source for time complexity analysis:
# https://cs.stackexchange.com/questions/96626/whats-the-big-o-runtime-of-a-dfs-word-search-through-a-matrix
class Solution:
    
    VISITED = "#"
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.contains_word(board, row, col, word, 0):
                        return True
        return False
    
    def contains_word(self, board, row, col, word, index):
        if (
            not self.is_valid_cell(board, row, col)
            or board[row][col] == self.VISITED
            or board[row][col] != word[index]
        ):
            return False
        if index == len(word) - 1:
            return True
        character = board[row][col]
        board[row][col] = self.VISITED
        
        for direction in self.DIRECTIONS:
            if self.contains_word(
                board, row + direction[0], col + direction[1], word, index + 1
            ):
                return True
        board[row][col] = character
        return False
    
    def is_valid_cell(self, board, row, col):
        num_rows = len(board)
        num_cols = len(board[0])
        if (
            row >= num_rows
            or row < 0
            or col >= num_cols
            or col < 0
        ):
            return False
        return True