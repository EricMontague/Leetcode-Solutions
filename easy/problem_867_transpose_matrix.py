"""This is my solution to Leetcode problem 867."""


#Overall time complexity: O(nm), where "n" is the number of rows and
#"m" is the number of columns

#Overall space complexity: O(nm)

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return A      
        result = [[None] * len(A) for col in A[0]]
        for row in range(len(A)):
            for col, value in enumerate(A[row]):
                result[col][row] = value
        return result
        

                    
        