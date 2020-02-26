"""My solution to problem 944 on Leetcode:
Delete Columns to Make Sorted.
"""

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        deletions = 0
        for letter in range(len(A[0])):
            for word in range(0, len(A) - 1):
                if A[word][letter] > A[word + 1][letter]:
                    deletions += 1
                    break
        return deletions

#Time complexity is O(n * m), where "n" is the number of
#words in the list and "m" is the number of letters in
#each word
#Space complexity is O(1)
        
