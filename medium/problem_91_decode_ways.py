"""This file contains my solutions to Leetcode problem 91: Decode Ways."""



# Bottom Up Space efficient
# time complexity: O(n), where 'n' is the length of the string
# space complexity: O(n)
class Solution:
    def numDecodings(self, encoded_string: str) -> int:
        if not encoded_string:
            return 1
        after_next = 1
        next_ = 1 if encoded_string[-1] != "0" else 0
        for index in range(len(encoded_string) - 2, -1, -1):
            if encoded_string[index] == "0":
                current = 0
            else:
                current = next_
            if encoded_string[index] == "1" or (
                encoded_string[index] == "2" and encoded_string[index + 1] < "7"
            ):
                current += after_next
            after_next = next_
            next_ = current
        return next_
        
                

# Bottom Up
# time complexity: O(n), where 'n' is the length of the string
# space complexity: O(n)
class Solution:
    def numDecodings(self, encoded_string: str) -> int:
        if not encoded_string:
            return 1
        decodings = [0] * (len(encoded_string) + 1)
        decodings[-1] = 1
        decodings[-2] = 1 if encoded_string[-1] != "0" else 0
        for index in range(len(encoded_string) - 2, -1, -1):
            if encoded_string[index] == "0":
                decodings[index] = 0
            else:
                decodings[index] = decodings[index + 1]
            if encoded_string[index] == "1" or (
                encoded_string[index] == "2" and encoded_string[index + 1] < "7"
            ):
                decodings[index] += decodings[index + 2]
        return decodings[0]
        
                

# Recursion + Memoization
# time complexity: O(n), where 'n' is the length of the string
# space complexity: O(n)
class Solution:
    def numDecodings(self, encoded_string: str) -> int:
        decodings = [None] * len(encoded_string)
        return self.calc_num_decodings(encoded_string, 0, decodings)
    
    def calc_num_decodings(self, string, index, decodings):
        if index >= len(string):
            return 1
        elif decodings[index] is not None:
            return decodings[index]
        elif string[index] == "0":
            result = 0
        elif index == len(string) - 1:
            result = 1
        else:
            num1 = self.calc_num_decodings(string, index + 1, decodings)
            num2 = 0
            if string[index] == "1" or (string[index] == "2" and string[index + 1] < "7"):
                num2 = self.calc_num_decodings(string, index + 2, decodings)
            result = num1 + num2
        decodings[index] = result
        return result
                