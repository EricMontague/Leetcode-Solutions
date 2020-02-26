"""My solution to problem 1337: The K weakest rows."""

#A much better solution that uses O(k) space and runs in O(mlogn + mlogk + klogk)
#is located at the below link(I take no credit for that solution). 
#Although, I think that since in the worst case, since k can equal m
#the time complexity might be able to be expressed as O(mlogn + mlogm)

#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/discuss/496713/Python-One-Liner-using-Sorting
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counter = {}
        #iterate through the matrix counting the number of ones in 
        #each row, O(mn)
        for row in range(len(mat)):
            counter.setdefault(row, 0)
            for col in mat[row]:
                if col == 1:
                    counter[row] += 1

        #sort the rows using the number of ones as the keys, O(mlogm)
        sorted_counter = sorted(counter.items(), key=lambda item: item[1])

        #get the first k items from the sorted_counter list, O(k)
        output = [sorted_counter[i][0] for i in range(k)]
        return output


#Note: m is the number of rows in the matrix, n is the number of columns
#Overall time complexity: O(mn + mlogm)
#Overall space complexity: O(m)

#time complexity explanation: The time complexity is O(mn + mlogm + k). This problem
#states that "k" is upper bounded by "m", but that doesn't matter because
#you drop lower order terms when determining the overall runtime of an algorithm,
#so the overall time complexity is O(mn + mlogm)

#space complexity explanation: The both counter and sorted counter will
#be of size "m", and output will be of size "k". This would lead to a space
#complexity of O(2m + k). However, the problem states that in the worst case,
#"k" would be equal to m, making this O(3m). After dropping the coefficient,
#you get the final space complexity of O(m)