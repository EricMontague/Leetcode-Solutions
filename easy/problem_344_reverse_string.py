"""This is my solution to problem 344: Reverse String."""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        low = 0
        high = len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1


#Overall time complexity: O(n), where "n" is the length of the string
#Explanation: Both pointers traverse exactly half of the list in tandem
#meaning that the time complexity is O(n / 2), which is just O(n)
#Overall space complexity: O(1)
#Explanation: This algorithm uses no auxillary space to reverse the string
