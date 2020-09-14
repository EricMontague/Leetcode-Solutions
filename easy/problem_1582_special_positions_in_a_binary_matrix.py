"""This file contains my solution to Leetcode problem 1582: Special Positions in a Binary Matrix."""

# time complexity: O(mn), where 'm' is the number of rows and 'n' is the number of columns
# space complexity: O(m + n), where 'm' is the number of rows and 'n' is the number of columns
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        numberOfOnesInRow, numberOfOnesInCol = self.buildFrequencyLists(mat)
        return self.findNumSpecialPositions(mat, numberOfOnesInRow, numberOfOnesInCol)
    
    def buildFrequencyLists(self, matrix):
        numberOfOnesInRow = [0] * len(matrix)
        numberOfOnesInCol = [0] * len(matrix[0])
        for rowIdx in range(len(matrix)):
            for colIdx in range(len(matrix[rowIdx])):
                numberOfOnesInRow[rowIdx] += matrix[rowIdx][colIdx]
                numberOfOnesInCol[colIdx] += matrix[rowIdx][colIdx]
        return numberOfOnesInRow, numberOfOnesInCol
        
    def findNumSpecialPositions(self, matrix, numberOfOnesInRow, numberOfOnesInCol):
        numSpecialPositions = 0
        for rowIdx in range(len(matrix)):
            for colIdx in range(len(matrix[rowIdx])):
                if matrix[rowIdx][colIdx] == 1:
                    if numberOfOnesInRow[rowIdx] == 1 and numberOfOnesInCol[colIdx] == 1:
                        numSpecialPositions += 1
        return numSpecialPositions
                
        