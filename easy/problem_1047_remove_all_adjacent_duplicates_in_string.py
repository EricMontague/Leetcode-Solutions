"""This is my solution to Leetcode problem 1047: Remove All Adjacent Duplicates In String."""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


#Overall time complexity: O(n), where n is the length of the input string
#Explanation: You have to iterate over all n characters in the input string,
#and all operations performed during each loop take O(1) time. Thus this
#leads to O(n) time complexity.

#Overal space complexity: O(n), where n is the length of the input string
#Explanation: In the worst case your stack will contain all characters in the input
#string if there are no duplicaties, meaning that the size of the stack is upper bounded
#by n, where n is the length of the input string.