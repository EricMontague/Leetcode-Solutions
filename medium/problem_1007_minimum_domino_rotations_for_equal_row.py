"""This is my solution to problem 1007: Minimum Domino Roations for Equal Row."""


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return -1
        first_domino = [A[0], B[0]]
        for value in first_domino:
            counter = self.countOccurrences(value, A, B)
            if counter[0] != -1:
                return self.calculateMinRotations(A, counter)
        return -1
    
    def countOccurrences(self, value, top_tiles, bottom_tiles):
        counter = [0, 0]
        for index in range(len(top_tiles)):
            if not self.inDomino(value, index, top_tiles, bottom_tiles):
                return [-1, -1]
            if top_tiles[index] == value:
                counter[0] += 1
            if bottom_tiles[index] == value:
                counter[1] += 1
        return counter
        
    def inDomino(self, value, index, top_tiles, bottom_tiles):
        if top_tiles[index] != value and bottom_tiles[index] != value:
            return False
        return True
    
    def calculateMinRotations(self, tiles, counter):
        return min(len(tiles) - counter[0], len(tiles) - counter[1])
    
#Overall time complexty: O(n), where "n" is the number of dominoes
#Explanation: At most this solution does two passes over the dominoes, leading to O(2n) time complexity
#which is just O(n)

#Overall space complexity: O(1)
#Explanation: Regardless of the number of dominoes given, the same list of size 2 is used, making
#the space constant.